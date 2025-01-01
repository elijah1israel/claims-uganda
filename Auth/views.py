from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from uuid import uuid4
from .models import RegistrationLink, ResetPasswordLink
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from .forms import RegistrationLinkForm
from django.contrib.auth.models import User
from Staff.models import Staff
from Assessors.models import Assessor
from claims.views import api
from uuid import uuid4
from .schema import LoginSchema, ChangePasswordSchema
from ninja.responses import Response
from .api import ApiKeyAuth

def login_user(request):
    """
    View to handle login of users. If the user is authenticated, redirects to the dashboard. If the user is not authenticated and the request is a POST, attempts to authenticate the user. If the user is authenticated and active, logs the user in and redirects to the dashboard. If the user is authenticated but inactive, shows an error message. If the user is not authenticated, shows an error message.

    :param request: The request object.
    :return: A redirect to the dashboard if the user is authenticated and active, or an HTTPResponse with the login form if the user is not authenticated.
    """
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.staff:
            if user.staff.status == 'Inactive':
                messages.error(request, 'Your account is inactive. Please contact the admin.')
                return redirect('.')
            else:
                login(request, user)
                messages.success(request, f'Welcome back {user.first_name}.')
                next = request.GET.get('next')
                if next:
                    return redirect(next)
                return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('.')
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')


def send_registration_link(request):
    """
    Handles the sending of a registration link to a user. If the request method is POST, it processes the form data 
    and creates a new RegistrationLink object. The registration link is set to expire in one day. Upon successful 
    creation, a success message is displayed and the user is redirected to the staff page.

    :param request: The request object containing the HTTP request data.
    :return: A redirect to the staff page.
    """
    if request.method == 'POST':
        form = RegistrationLinkForm(request.POST)
        if form.is_valid():
            registration_link = form.save(commit=False)
            registration_link.expires_at = timezone.now() + timedelta(days=1)
            registration_link.save()
            link_url = reverse('register_user', kwargs={'token': registration_link.token})
            print(link_url)
            messages.success(request, 'Registration link sent successfully.')
    return redirect('staff')

def account_settings(request):
    return render(request, 'account_settings.html')


def register_user(request, token):
    link = RegistrationLink.objects.filter(token=token).first()
    if link is None:
        return redirect('login')
    if link.expires_at < timezone.now():
        return redirect('login')
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('.')
        else:
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=link.email, email=link.email, password=password)
            user.save()
            staff = Staff.objects.create(user=user, department=link.department)
            staff.save()
            if link.department == 'Assessors':
                assessor = Assessor.objects.create(staff=staff)
                assessor.save()
            link.delete()
            messages.success(request, 'Registration successful. You can now login.')
            return redirect('login')
    return render(request, 'register.html', {'token': token})


def password_reset(request):
    if request.method == 'POST':
        email = request.POST['email']
        user = User.objects.filter(email=email).first()
        if user is None:
            messages.error(request, 'User does not exist.')
            return redirect('password_reset')
        else:
            reset_password_link = ResetPasswordLink.objects.create(user=user, expires_at=timezone.now() + timedelta(days=1))
            reset_password_link.save()
            link_url = reverse('reset_password', kwargs={'token': str(reset_password_link.token)})
            print(link_url)
            messages.success(request, 'Check your email for reset instructions.')
            return redirect('login')
    return render(request, 'password_reset.html')


def reset_password(request, token):
    link = ResetPasswordLink.objects.filter(token=token).first()
    if link is None:
        messages.error(request, 'Invalid reset link.')
        return redirect('login')
    if link.expires_at < timezone.now():
        messages.error(request, 'Reset link has expired.')
        return redirect('login')
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('.')
        else:
            user = link.user
            user.set_password(password)
            user.save()
            link.delete()
            messages.success(request, 'Password reset successful. You can now login.')
            return redirect('login')
    return render(request, 'reset_password.html', {'token': token})



def change_password(request):
    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
        if new_password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('.')
        else:
            user = request.user
            if user.check_password(current_password):
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Password changed successfully.')
                return redirect('login')
            else:
                messages.error(request, 'Current password is incorrect.')
                return redirect('.')


@api.post('/auth/login')
def login_endpoint(request, payload: LoginSchema):
    user = authenticate(request, username=payload.email, password=payload.password)
    if user is not None and user.staff:
        user.staff.api_key = uuid4()
        user.staff.save()
        data = {
            'message': 'Login successful',
            'api_key': user.staff.api_key,
            'id': user.id
            }
        return Response(data)
    else:
        data = {'message': 'Incorrect email or password'}
        return Response(data, status=401)


@api.post('/auth/change/password', auth=ApiKeyAuth())
def change_password_endpoint(request, payload: ChangePasswordSchema):
    if payload.new_password == payload.confirm_password:
        user = request.auth
        if user.check_password(payload.old_password):
            user.set_password(payload.new_password)
            user.staff.api_key = uuid4()
            user.save()
            user.staff.save()
            data = {'message': 'Password reset successfully.'}
            return data
        else:
            data = {
                'message': 'The old password is incorrect'
            }
            return Response(data, status=401)
    else:
        data = {
            'message': 'Password do not match'
        }
        return Response(data, status=500)
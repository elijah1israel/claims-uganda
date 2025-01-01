from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Staff
from Auth.forms import RegistrationLinkForm
from .models import departments
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required
def staff(request):
    staff_list = Staff.objects.all()
    paginator = Paginator(staff_list, 10)  # Show 10 staff per page
    page_number = request.GET.get('page')
    if not page_number:
        page_number = 1
    page_obj = paginator.get_page(page_number)
    return render(request, 'staff.html', {'staff': page_obj, 'form': RegistrationLinkForm()})


@login_required
def make_staff_inactive(request, pk):
    staff = Staff.objects.get(pk=pk)
    staff.status = 'Inactive'
    staff.save()
    messages.success(request, 'Staff account deactivated successfully.')
    return redirect('staff')


@login_required
def make_staff_active(request, pk):
    staff = Staff.objects.get(pk=pk)
    staff.status = 'Active'
    staff.save()
    messages.success(request, f'Staff account activated successfully.')
    return redirect('staff')


@login_required
def staff_profile(request, pk):
    staff = Staff.objects.get(pk=pk)
    return render(request, 'staff_profile.html', {'staff': staff, 'departments': departments})


@login_required
def upload_profile_picture(request):
    if request.method == 'POST':
        image = request.FILES['image']
        staff = request.user.staff
        staff.profile_picture = image
        staff.save()
        messages.success(request, 'Profile picture uploaded successfully.')
    return redirect('staff_profile', pk=request.user.staff.pk)


@login_required
def change_department(request, staff_id):
    staff = Staff.objects.get(pk=staff_id)
    staff.department = request.POST['department']
    staff.save()
    messages.success(request, f"{staff.user.first_name} has been successfully added to the {request.POST['department']} Department.")
    return redirect('staff_profile', pk=staff_id)


@login_required
def delete_profile_picture(request):
    staff = request.user.staff
    staff.profile_picture = None
    staff.save()
    messages.success(request, 'Profile picture deleted successfully.')
    return redirect('staff_profile', pk=request.user.staff.pk)

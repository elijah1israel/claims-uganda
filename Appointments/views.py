from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import AppointmentForm
from django.contrib import messages
from .models import Appointment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required
def appointments(request):
    appointments = request.user.staff.appointments.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(appointments, 10)
    try:
        appointments = paginator.page(page)
    except PageNotAnInteger:
        appointments = paginator.page(1)
    except EmptyPage:
        appointments = paginator.page(paginator.num_pages)

    return render(request, 'appointments.html', {'form': AppointmentForm(), 'appointments': appointments})

@login_required
def schedule_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.staff = request.user.staff
            form.save()
            form.instance.staff.appointments.add(form.instance)
            messages.success(request, 'Appointment scheduled successfully.')
            return redirect('appointments')
    else:
        form = AppointmentForm()
    return render(request, 'schedule_appointment.html', {'form': form})


@login_required
def delete_all_appointments(request):
    Appointment.objects.filter(staff=request.user.staff).delete()
    messages.success(request, 'All appointments deleted successfully.')
    return redirect('dashboard')

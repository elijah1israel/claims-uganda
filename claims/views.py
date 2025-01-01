from django.shortcuts import render
from Staff.models import Staff
from plotly import graph_objs as go
from Cases.models import Case
from django.utils.timezone import now
from Appointments.forms import AppointmentForm
from FeeNotes.forms import FeeNoteForm
from FeeNotes.models import FeeNote
from django.contrib.auth.decorators import login_required
from Reports.models import Report
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ninja import NinjaAPI

api = NinjaAPI()

@login_required
def dashboard(request):
    cases = Case.objects.all()      
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    data = []
    for month in months:
        if request.user.staff.department == 'Assessors':
            data.append(Case.objects.filter(date_reported__month=months.index(month)+1, date_reported__year=now().year, assessor=request.user.staff.assessor).count())
        else:
            data.append(Case.objects.filter(date_reported__month=months.index(month)+1, date_reported__year=now().year).count())
    fig = go.Figure(data=[go.Bar(y=data, x=months)])
    fig.update_layout(title=f'Cases handled per month ({now().year})', xaxis_title='Month', yaxis_title='Count')
    div = fig.to_html(full_html=False)
    staff = Staff.objects.all().count()
    fee_note_form = FeeNoteForm()
    if request.user.staff.department == 'Assessors':
        fee_note_form.fields['case'].queryset = FeeNoteForm().fields['case'].queryset.filter(assessor=request.user.staff.assessor, fee_note=None)
    appointments = request.user.staff.appointments.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(appointments, 4)
    try:
        appointments = paginator.page(page)
    except PageNotAnInteger:
        appointments = paginator.page(1)
    except EmptyPage:
        appointments = paginator.page(paginator.num_pages)
    return render(request, 'dashboard.html', {'staff_count': staff, 'div': div, 'cases': cases, 'appointment_form': AppointmentForm(), 'fee_note_form': fee_note_form, 'case_count': Case.objects.all().count(), 'fee_note_count': FeeNote.objects.all().count(), 'report_count': Report.objects.all().count(), 'appointments': appointments})


@api.get('/')
def root(request):
    return 'Claims api v1'
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ReportForm
from Cases.models import Case
from .models import Report
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required
def upload_report(request, case_id):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.case = Case.objects.get(id=case_id)
            report.save()
            report.case.reports.add(report)
            report.case.assessor.reports.add(report)
            messages.success(request, f'{report.report_type} Report uploaded successfully.')
            return redirect('case_info', case_id=case_id)
    else:
        form = ReportForm()
    return render(request, 'upload_report.html', {'form': form})


@login_required
def reports(request):
    if request.user.staff.department == 'Assessors':
        reports = request.user.staff.assessor.reports.all()
    else:
        reports = Report.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(reports, 10)
    try:
        reports = paginator.page(page)
    except PageNotAnInteger:
        reports = paginator.page(1)
    except EmptyPage:
        reports = paginator.page(paginator.num_pages)
    return render(request, 'reports.html', {'reports': reports})


@login_required
def download_report(request, report_id):
    report = Report.objects.get(id=report_id)
    response = HttpResponse(report.file)
    response['Content-Disposition'] = f'attachment; filename="{report.file.name}"'
    return response


@login_required
def delete_report(request, report_id):
    """
    Deletes a report and redirects to the referring page, or the reports page if there is no referring page.

    :param request: The request object.
    :param report_id: The id of the report to delete.
    :return: A redirect response to the referring page or the reports page.
    """
    report = Report.objects.get(id=report_id)
    report.delete()
    messages.success(request, f'{report.report_type} Report deleted successfully.')
    return redirect(request.META.get('HTTP_REFERER', 'reports'))


@login_required
def report_info(request, report_id):
    report = Report.objects.get(id=report_id)
    return render(request, 'report_info.html', {'report': report})


@login_required
def submit_report(request, report_id):
    """
    Handles the submission of a report by updating its status, creating a submission entry, and adding a comment.

    :param request: The HTTP request object containing request data.
    :param report_id: The ID of the report to be submitted.
    :return: A redirect to the report information page upon successful submission.
    """
    report = Report.objects.get(id=report_id)
    if request.method == 'POST':
        comment = request.POST.get('comment')
        submission = report.submissions.create(report=report)
        report.status = 'Submitted'
        report.save()
        submission.comments.create(text=comment, report=report, author=request.user.staff)
        messages.success(request, 'Report submitted successfully.')
        return redirect('report_info', report_id=report_id)

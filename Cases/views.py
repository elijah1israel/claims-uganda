from django.shortcuts import render, redirect
from .models import Case
from .forms import CaseForm
from Reports.forms import ReportForm
from django.contrib import messages
from SupportDocuments.forms import SupportDocumentForm
from zipfile import ZipFile
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from claims.views import api
from Auth.api import ApiKeyAuth

@login_required
def cases(request):
    if request.user.staff.department == 'Assessors':
        cases = request.user.staff.assessor.cases.all()
    else:
        cases = Case.objects.all()
    paginator = Paginator(cases, 10)
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    context = {
        'page_obj': page_obj,
        'form': CaseForm()
    }
    return render(request, 'cases.html', context)

@login_required
def comment_case(request, case_id):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        case = Case.objects.get(id=case_id)
        case.comment = comment
        case.save()
        messages.success(request, 'Comment added successfully.')
        return redirect('case_info', case_id=case_id)

@login_required
def new_case(request):
    if request.method == 'POST':
        form = CaseForm(request.POST)
        if form.is_valid():
            case = form.save()
            case.reference_number = f'{case.insurance_Company}/{case.policy}/{case.id}/{case.date_reported.year}'
            case.save()
            assessor = form.cleaned_data['assessor']
            assessor.cases.add(form.instance)
            messages.success(request, 'Case created successfully.')
            return redirect('cases')
    else:
        form = CaseForm()
    return render(request, 'new_case.html', {'form': form})

@login_required
def edit_case(request, case_id):
    case = Case.objects.get(id=case_id)
    if request.method == 'POST':
        form = CaseForm(request.POST, instance=case)
        if form.is_valid():
            form.save()
            return redirect('cases')
    else:
        form = CaseForm(instance=case)
    return render(request, 'edit_case.html', {'form': form})

@login_required
def case_info(request, case_id):
    case = Case.objects.get(id=case_id)
    return render(request, 'case_info.html', {'case': case, 'report_form': ReportForm(), 'support_document_form': SupportDocumentForm()})

@login_required
def zip_case_files(request, case_id):
    case = Case.objects.get(id=case_id)
    with ZipFile('case_files.zip', 'w') as zip_file:
        for document in case.support_documents.all():
            zip_file.write(document.file.path, document.name)
        for picture in case.pictures.all():
            zip_file.write(picture.image.path, picture.image.name)
        for report in case.reports.all():
            zip_file.write(report.file.path, report.file.name)
    with open(f'case_files.zip', 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename=case_files.zip'
        return response

@login_required
def delete_case(request, case_id):
    case = Case.objects.get(id=case_id)
    case.delete()
    messages.success(request, 'Case deleted successfully.')
    return redirect('cases')

@login_required
def edit_case(request, case_id):
    case = Case.objects.get(id=case_id)
    assessor = case.assessor
    if request.method == 'POST':
        form = CaseForm(request.POST, instance=case)
        if form.is_valid():
            if form.cleaned_data['assessor'] != assessor:
                assessor.cases.remove(case)
                for report in case.reports.all():
                    report.assessor = form.cleaned_data['assessor']
                    report.save()
                    assessor.reports.remove(report)
                    form.cleaned_data['assessor'].reports.add(report)
                assessor.fee_notes.remove(case.fee_note)
                form.cleaned_data['assessor'].fee_notes.add(case.fee_note)
                assessor = form.cleaned_data['assessor']
                assessor.cases.add(form.instance)
                messages.success(request, 'Case assigned to new assessor successfully.')
            else:
                messages.success(request, 'Case edited successfully.')
            form.save()
            return redirect('cases')
    else:
        form = CaseForm(instance=case)
    messages.error(request, 'Failed to edit case.')
    return redirect('case_info', case_id=case_id)


@api.get('/cases', auth=ApiKeyAuth())
def cases_endpoint(request):
    user = request.auth
    if user.staff.department == 'Assessors':
        data = [
            {'id': c.id,
            'reference_number': c.reference_number,
            'insurance_company': c.insurance_Company,
            'policy': c.policy
            }
             for c in user.staff.assessor.cases.all()
            ]
        return data
    else:
        data = [
            {'id': c.id,
            'reference_number': c.reference_number,
            'insurance_company': c.insurance_Company,
            'policy': c.policy
            }
            for c in Case.objects.all()]
        return data
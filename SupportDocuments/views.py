from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import SupportDocument
from .forms import SupportDocumentForm
from django.contrib import messages
from Cases.models import Case

@login_required
def upload_support_document(request, case_id):
    case = Case.objects.get(id=case_id)
    if request.method == 'POST':
        form = SupportDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.case = case
            document.save()
            case.support_documents.add(document)
            messages.success(request, 'Support document uploaded successfully.')
            return redirect('case_info', case_id=case_id)
    else:
        form = SupportDocumentForm()
    messages.error(request, 'Failed to upload support document.')
    return redirect('case_info', case_id=case_id)


@login_required
def delete_support_document(request, document_id):
    document = SupportDocument.objects.get(id=document_id)
    document.delete()
    messages.success(request, 'Support document deleted successfully.')
    return redirect('case_info', case_id=document.case.id)

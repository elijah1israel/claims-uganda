from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import FeeNote
from .forms import FeeNoteForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required
def fee_notes(request):
    form = FeeNoteForm()
    if request.user.staff.department == 'Assessors':
        form.fields['case'].queryset = form.fields['case'].queryset.filter(assessor=request.user.staff.assessor, fee_note=None)
        fee_notes = request.user.staff.assessor.fee_notes.all()
    else:
        fee_notes = FeeNote.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(fee_notes, 10)
    try:
        fee_notes = paginator.page(page)
    except PageNotAnInteger:
        fee_notes = paginator.page(1)
    except EmptyPage:
        fee_notes = paginator.page(paginator.num_pages)
    return render(request, 'fee_notes.html', {'form': form, 'fee_notes': fee_notes})


@login_required
def add_fee_note(request):
    if request.method == 'POST':
        form = FeeNoteForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            total = form.instance.inspection_and_assessment_fee + form.instance.accommodation_fee + form.instance.out_of_office_allowance + form.instance.travel_and_assessment_fee + form.instance.photos
            vat = 0.18*float(total)
            form.instance.total = float(total) - vat
            form.instance.value_added_tax = vat
            print(form.instance.total)
            form.save()
            form.instance.case.fee_note = form.instance
            form.instance.case.assessor.fee_notes.add(form.instance)
            form.instance.case.save()
            messages.success(request, 'Fee note added successfully.')
            return redirect('fee-notes')
    else:
        form = FeeNoteForm()
    return render(request, 'fee_notes.html', {'form': form})


def upload_fee_note(request, fee_note_id):
    fee_note = FeeNote.objects.get(id=fee_note_id)
    if request.method == 'POST':
        file = request.FILES['file']
        fee_note.valid_fee_note = file
        fee_note.save()
        messages.success(request, 'Fee note uploaded successfully.')
        return redirect(request.META.get('HTTP_REFERER', 'fee-notes'))
    else:
        form = FeeNoteForm(instance=fee_note)
        return render(request, 'fee_notes.html', {'form': form})
            


@login_required
def mark_fee_note_as_paid(request, fee_note_id):
    fee_note = FeeNote.objects.get(id=fee_note_id)
    fee_note.status = 'Paid'
    fee_note.save()
    messages.success(request, 'Fee note marked as paid.')
    return redirect(request.META.get('HTTP_REFERER', 'fee-notes'))

    
@login_required
def delete_fee_note(request, fee_note_id):
    fee_note = FeeNote.objects.get(id=fee_note_id)
    fee_note.delete()
    messages.success(request, 'Fee note deleted successfully.')
    return redirect(request.META.get('HTTP_REFERER', 'fee-notes'))

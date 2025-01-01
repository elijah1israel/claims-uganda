from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Picture
from Cases.models import Case
from django.contrib import messages

@login_required
def upload_picture(request, case_id):
    if request.method == 'POST':
        picture = request.FILES['picture']
        caption = request.POST['caption']
        case = Case.objects.get(id=case_id)
        picture = Picture.objects.create(case=case, image=picture, caption=caption)
        picture.save()
        case.pictures.add(picture)
        messages.success(request, 'Picture uploaded successfully.')
        return redirect('case_info', case_id=case_id)


@login_required
def delete_picture(request, picture_id):
    picture = Picture.objects.get(id=picture_id)
    picture.delete()
    messages.success(request, 'Picture deleted successfully.')
    return redirect('case_info', case_id=picture.case.id)
    
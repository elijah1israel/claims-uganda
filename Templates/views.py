from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Template
from .forms import TemplateForm
from django.contrib import messages


@login_required
def templates(request):
    templates = Template.objects.all()
    return render(request, 'templates.html', {'templates': templates, 'form': TemplateForm()})


@login_required
def upload_template(request):
    if request.method == 'POST':
        form = TemplateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Template uploaded successfully.')
            return render(request, 'templates.html', {'templates': Template.objects.all(), 'form': TemplateForm()})
        else:
            messages.error(request, 'Template upload failed.')
    return render(request, 'templates.html', {'templates': Template.objects.all(), 'form': TemplateForm()})


@login_required
def delete_template(request, template_id):
    """
    Deletes a template with the given template_id from the database.

    Args:
        request: The HTTP request object.
        template_id: The ID of the template to be deleted.

    Returns:
        HttpResponse: A response object that renders the templates page, displaying
        a success message and the updated list of templates.
    """
    template = Template.objects.get(id=template_id)
    template.delete()
    messages.success(request, 'Template deleted successfully.')
    return render(request, 'templates.html', {'templates': Template.objects.all(), 'form': TemplateForm()})


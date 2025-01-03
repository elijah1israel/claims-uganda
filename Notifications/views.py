from django.shortcuts import render

def view_notifications(request):
    return render(request, 'notifications.html')
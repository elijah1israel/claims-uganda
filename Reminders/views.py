from django.shortcuts import render

def reminders(request):
    return render(request, 'reminders.html')
from django.shortcuts import render
from .models import Job

def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})

def eda(request):
    return render(request, 'jobs/eda.html')

def investigate_data_set(request):
    return render(request, 'jobs/investigate_data_set.html')

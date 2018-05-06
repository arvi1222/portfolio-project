from django.shortcuts import render
from .models import Job

def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})

def eda(request):
    return render(request, 'jobs/eda.html')

def investigate_data_set(request):
    return render(request, 'jobs/investigate_data_set.html')

def data_visualization(request):
    return render(request, 'jobs/data_visualization.html')

def data_wrangling(request):
    return render(request, 'jobs/data_wrangling.html')

def machine_learning(request):
    return render(request, 'jobs/machine_learning.html')

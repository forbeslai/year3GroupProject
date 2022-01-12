from django.shortcuts import render
from .helper import FieldLookup
from .models import Customer, Worker, Services, Bill, ProjectBillDetails, ProjectBillBridge, Project, WorkerProjectBridge
import datetime

# Create your views here.
from django.http import HttpResponse

def index(request):
    context_dict = {}
    return render(request, 'imaging_system_app/index.html', context=context_dict)

def services(request):
    context_dict = {}
    return render(request, 'imaging_system_app/services.html', context=context_dict)

def projects(request):
    context_dict={}
    return render(request, 'imaging_system_app/projects.html', context=context_dict)

def customers(request):
    context_dict={}
    return render(request, 'imaging_system_app/customers.html', context=context_dict)

def bills(request):
    context_dict={}
    return render(request, 'imaging_system_app/bills.html', context=context_dict)
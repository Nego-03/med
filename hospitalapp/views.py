from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def starter(request):
    return render(request, 'starter-page.html')
def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')
def department(request):
    return render(request, 'departments.html')

def doctor(request):
    return render(request, 'doctor.html')
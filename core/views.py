from django.shortcuts import render
from .models import Project, Skill, Contact

def home(request):
    skills = Skill.objects.all()
    projects = Project.objects.all()
    return render(request, 'home.html', {'skills': skills, 'projects': projects})

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        Contact.objects.create(name=name, email=email, message=message)
    return render(request, 'contact.html')


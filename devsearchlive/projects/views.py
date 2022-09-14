from multiprocessing import context
from django.shortcuts import render
from .models import Project

projectList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website',
        'topRated': True
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website',
        'topRated': False
    },
    {
        'id': '1',
        'title': 'Social Network',
        'description': 'An open source project built by the community',
        'topRated': True
    },

]

# Create your views here.
def projects(request):
    projects = Project.objects.all()
    print("Project:", projects)
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    context = { 'project': projectObj, 'tags': tags }
    return render(request, 'projects/single-project.html', context)
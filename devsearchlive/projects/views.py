from multiprocessing import context
from django.shortcuts import render
from .models import Project
from .forms import ProjectForm

# Create your views here.
def projects(request):
    projects = Project.objects.all()
    print("Project:", projects)
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    reviews = projectObj.reviews.all()
    context = { 'project': projectObj, 'tags': tags, 'reviews': reviews }
    return render(request, 'projects/single-project.html', context)


def createProject(request):
    form = ProjectForm()
    context = {'form': form}

    return render(request, 'projects/project-form.html', context)
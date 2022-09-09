from django.shortcuts import render

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
    context = {'projects': projectList}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObejct = None
    for i in projectList:
        if i['id'] == str(pk):
            projectObejct = i
    return render(request, 'projects/single-project.html',{'project': projectObejct})
from django.shortcuts import render
from projects.models import Project, Technology

# Create your views here.
def project_index(request):
    """Show the homescreen of all the projects"""
    projects = Project.objects.all()
    technology = Technology.objects.all();
    context = {
        'projects': projects,
        'technology': technology
    }
    return render(request, 'projects/project_index.html', context)

def project_detail(request, pk):
    """Show the individual project details"""
    project = Project.objects.get(id=pk)
    context = {
        'project': project
    }
    return render(request, 'projects/project_detail.html', context)
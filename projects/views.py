from django.shortcuts import render
from projects.models import Project, Technology
import requests

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

    # api call for repo languages
    languages = {}
    repoUrl = project.link
    r = requests.get("https://api.github.com/repos/" + repoUrl[repoUrl.index(".com/")+5:] + "/languages")
    if r.status_code == 200:
        languages = r.json()

    context = {
        'project': project,
        'languages': languages
    }
    return render(request, 'projects/project_detail.html', context)
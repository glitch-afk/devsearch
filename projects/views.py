from django.shortcuts import render
from .models import Project

projectsList = [
    {
        "id": "1",
        "title": "Ecommerce Website",
        "description": "Alias omnis ut laboriosam a placeat. Impedit harum odit aperiam blanditiis. Ut sit aliquam aut voluptatem illum est dicta dolores",
    },
    {
        "id": "2",
        "title": "Portfolio Website",
        "description": "Alias omnis ut laboriosam a placeat. Impedit harum odit aperiam blanditiis. Ut sit aliquam aut voluptatem illum est dicta dolores",
    },
    {
        "id": "3",
        "title": "Social Network",
        "description": "Alias omnis ut laboriosam a placeat. Impedit harum odit aperiam blanditiis. Ut sit aliquam aut voluptatem illum est dicta dolores",
    },
]


def projects(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "projects/projects.html", context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, "projects/project.html", {"project": projectObj})

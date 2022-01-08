from django.shortcuts import render

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
    number = 11
    page = "Projects"
    context = {"page": page, "number": number, "projects": projectsList}
    return render(request, "projects/projects.html", context)


def project(request, pk):
    projectObj = None
    for i in projectsList:
        if i["id"] == pk:
            projectObj = i
    return render(request, "projects/project.html", {"project": projectObj})

from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from .forms import ProjectForm


# PUBLIC VIEWS

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'projects/project_detail.html', {'project': project})


# ADMIN / CMS VIEWS

@staff_member_required
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_projects')
    else:
        form = ProjectForm()

    return render(request, 'projects/add_project.html', {'form': form})


@staff_member_required
def manage_projects(request):
    projects = Project.objects.all()
    return render(request, 'projects/manage_projects.html', {'projects': projects})


@staff_member_required
def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('manage_projects')
    else:
        form = ProjectForm(instance=project)

    return render(request, 'projects/edit_project.html', {'form': form})


@staff_member_required
def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if request.method == 'POST':
        project.delete()
        return redirect('manage_projects')

    return render(request, 'projects/delete_project.html', {'project': project})
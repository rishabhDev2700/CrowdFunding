from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from user_dashboard.forms import ProjectForm
from user_dashboard.models import Project


@login_required
def dashboard(request):
    my_projects = Project.objects.filter(owner=request.user)
    return render(request, 'user_dashboard/dashboard.html', {'my_projects': my_projects})


@login_required
def new_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=Project(owner=request.user))
        if form.is_valid():
            form.save()
            messages.success(request, 'Project Created Successfully')
            return redirect('projects')
        else:
            messages.error(request, 'Failed to Create Project')
    form = ProjectForm()
    return render(request, 'user_dashboard/project_form.html', {'form': form})


@login_required
def update_project(request, pk):
    try:
        instance = Project.objects.get(pk=pk)
        form = ProjectForm(instance=instance)
    except ObjectDoesNotExist:
        messages.error(request, 'Project not found')
        return redirect('project form')
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Updated Project')
            return redirect('dashboard')
        messages.error(request, 'Some Error Occurred')
        return redirect('projects')
    return render(request, 'user_dashboard/project_form.html', {'form': form})


def projects(request):
    all_projects = Project.objects.all()
    return render(request, 'user_dashboard/projects.html', {'all_projects': all_projects})


def project_details(request, project_id):
    project = Project.objects.get(pk=project_id)
    return render(request, 'user_dashboard/project_details.html', {'project': project})


@login_required
def contribute_to_project(request, project_id):
    project = Project.objects.get(pk=project_id)
    return render(request, 'user_dashboard/contribution_form.html', {'project': project, })

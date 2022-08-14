from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('new_project/', views.new_project, name="project form"),
    path('update_project/<int:pk>', views.update_project, name="project update"),
    path('', views.projects, name='projects'),
    path('project/<int:project_id>/', views.project_details, name="project details"),
    path('project/contribute/<int:project_id>/', views.contribute_to_project, name="contribute to"),
]

from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('new_project/', views.new_project, name="project form"),
    path('update_project/<int:pk>', views.update_project, name="project update"),
    path('projects/', views.projects, name='projects')
]

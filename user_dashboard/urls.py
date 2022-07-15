from django.urls import path
from . import views
urlpatterns = [
     path('dashboard/',views.dashboard,name="dashboard"),
     path('projects/',views.dashboard,name="projects"),
     path('settings/',views.dashboard,name="dashboard"),
 ]
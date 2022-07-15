from django.forms import ModelForm
from user_dashboard.models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'description', 'target', 'goals')

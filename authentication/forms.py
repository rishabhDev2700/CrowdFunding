from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm

from authentication.models import CustomUser, UserProfile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('bio','occupation','picture','contact','location')
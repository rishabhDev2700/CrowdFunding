from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from authentication.forms import CustomUserCreationForm, CustomUserChangeForm
from authentication.models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)

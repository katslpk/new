from functools import singledispatch
from typing import Text

from django import forms
from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.onboarding.models import AuthProfile
from apps.onboarding.models import Profile


@singledispatch
def a(obj) -> Text:
    return str(obj)


class AuthProfileAdminForm(forms.ModelForm):
    class Meta:
        model = AuthProfile
        fields = "__all__"
        widgets = {}


@admin.register(AuthProfile)
class AuthProfileAdminModel(ModelAdmin):
    readonly_fields = [
        a(f)
        for f in (
            AuthProfile.user,
            AuthProfile.verification_code,
            AuthProfile.verified_at,
        )
    ]


class ProfileAdminForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        widgets = {}


@admin.register(Profile)
class ProfileAdminModel(ModelAdmin):
    readonly_fields = [a(f) for f in (Profile.user,)]

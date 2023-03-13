from django.contrib.auth.forms import forms
from django.contrib.auth.models import User
from user_profile.models import Profile


class UpdateUserData(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']


class UpdateUserProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image']




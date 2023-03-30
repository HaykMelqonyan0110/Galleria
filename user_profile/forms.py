from django.contrib.auth.forms import forms
from django.contrib.auth.models import User
from user_profile.models import Profile
from business_account.models import BusinessAccountOrders


class UpdateUserData(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateUserProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'gender_fields', 'phone_number', 'address']






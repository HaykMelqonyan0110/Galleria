from .models import BusinessAccount
from django import forms


class RegisterForBusinessAccount(forms.ModelForm):
    class Meta:
        model = BusinessAccount
        fields = ['company_name', 'company_email', 'company_phone', 'company_image']


class UpdateAccountData(forms.ModelForm):
    class Meta:
        model = BusinessAccount
        fields = ['company_name',
                  'company_email',
                  'company_phone',
                  ]


class UpdateAccountImage(forms.ModelForm):
    class Meta:
        model = BusinessAccount
        fields = ['company_image']

from django import forms
from ecomstore.accounts.models import UserProfile

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        exclude = ('user',)

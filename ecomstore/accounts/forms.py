from django import forms
from ecomstore.accounts.models import UserProfile
from django.contrib.auth.forms import UserCreationForm

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        exclude = ('user',)

class RegistrationForm(UserCreationForm):
    password1 = forms.RegexField(label="Password", regex=r'^(?=.*\W+).*$',
                                 help_text='Password must be six characters \
                                            long and contain at least one \
                                            non-alphanumeric character.',
                                 widget=forms.PasswordInput, min_length=6,
                                 #render_value=False
                                 )
    password2 = forms.RegexField(label="Password confirmation", 
                                 regex=r'^(?=.*\W+).*$',
                                 widget=forms.PasswordInput, min_length=6,
                                 #render_value=False
                                 )
    email = forms.EmailField(max_length="50")

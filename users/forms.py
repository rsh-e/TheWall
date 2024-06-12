# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import datetime

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    dob = forms.DateField(input_formats=['%d/%m/%Y'], widget=forms.DateInput(format='%d/%m/%Y'))
    invitation_number = forms.CharField(max_length=6, min_length=6)

    def clean_dob(self):
        dob = self.cleaned_data['dob']
        if (dob.year + 16) > datetime.date.today().year:
            raise forms.ValidationError('You must be at least 16 to register')
        return dob

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'dob', 'invitation_number']
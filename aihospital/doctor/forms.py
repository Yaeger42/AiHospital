"""Doctor forms"""
# Django imports
from django import forms

# Models import
from django.contrib.auth.models import User
from doctor.models import Profile


class SignupForm(forms.Form):
    """Signup form"""
    username = forms.CharField(min_length=4, max_length=30)
    password = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )
    passwordConfirmation = forms.CharField(max_length=70,
                                           widget= forms.PasswordInput())
    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)

    email = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput()
    )
    bDay = forms.DateField(required=False, label='YYYY-MM-DD')

    def clean_username(self):
        """Username must be unique"""
        username = self.cleaned_data['username']
        usernameTaken = User.objects.filter(username=username).exists()
        if usernameTaken:
            raise forms.ValidationError('Username is already in use.')
        return username

    def clean(self):
        """Verify the passwords match"""
        data = super().clean()
        password = data['password']
        passwordConfirmation = data['passwordConfirmation']

        if password != passwordConfirmation:
            raise forms.ValidationError('Passwords do not match.')
        return data

    def save(self):
        """Create user and profile"""
        data = self.cleaned_data
        data.pop('passwordConfirmation')
        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()


class ProfileForm(forms.Form):
    """Profile form"""
    specialty = forms.CharField(max_length=200, required=True, label='Specialty')
    phoneNumber = forms.CharField(max_length=30, required=True, label='Phone Number')
    cedMed = forms.CharField(max_length=30, required=True, label='Medical ID license')
    bDay = forms.DateField(required=False, label='YYYY-MM-DD')
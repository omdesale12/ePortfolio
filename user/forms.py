from django import forms
from django.contrib.auth import get_user_model
User=get_user_model()
from django.contrib.auth.forms import UserCreationForm
from . models import UserProfile

class UserRegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['email','full_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = ''
        self.fields['password1'].widget.attrs.update({'autocomplete': 'new-password'})
        self.fields['password2'].widget.attrs.update({'autocomplete': 'new-password'})

class UpdateUserProfile(forms.ModelForm):
    class Meta:
        model=UserProfile
        exclude=['user']
    def save(self, commit=True):
        instance = super(UpdateUserProfile, self).save(commit=False)
        user = self.initial.get('user') if 'user' in self.initial else None

        if user:
            instance.user = user

        if commit:
            instance.save()

        return instance


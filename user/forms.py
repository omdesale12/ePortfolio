from django import forms
from django.contrib.auth import get_user_model
User=get_user_model()
from django.contrib.auth.forms import UserCreationForm
from . models import UserProfile,UserSocials

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


    
class AddSocial(forms.ModelForm):
    class Meta:
        model=UserSocials
        exclude = ['user']  # Exclude the 'user' field from the form

    # def save(self, commit=True, request=None):
    #     # Set the user field to the UserProfile of the provided request user
    #     instance = super(AddSocial, self).save(commit=False)
    #     if request and request.user.is_authenticated:
    #         instance.user = request.user.userprofile  # Assuming UserProfile is linked to User
    #     if commit:
    #         instance.save()
    #     return instance

from django import forms
from django.contrib.auth import get_user_model
User=get_user_model()
from django.contrib.auth.forms import UserCreationForm
from . models import UserProfile,UserSocials
from main.models import portfolio,resume,Education


class UserRegisterForm(UserCreationForm):
    full_name = forms.CharField(
        label="Full Name",
        widget=forms.TextInput(attrs={'placeholder': 'Full Name', 'class': 'form-control', 'style': 'padding: 5px;'}),
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control', 'style': 'padding: 5px;'}),
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control', 'style': 'padding: 5px;'}),
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-control', 'style': 'padding: 5px;'}),
    )
    
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
from django.utils import timezone
class AddPortfolio(forms.ModelForm):
    class Meta:
        model=portfolio
        exclude=['user','date_created']

    def save(self, commit=True):
        instance = super().save(commit=False)
        
        # Set the 'date_created' field to the current time
        instance.date_created = timezone.now()
        
        if commit:
            instance.save()
        return instance


class AddEducation(forms.ModelForm):
    class Meta:
        model=Education
        exclude=['user']


class AddResume(forms.ModelForm):
    class Meta:
        model=resume
        exclude=['user','uploaded_at']

        def save(self, commit=True):
            instance = super().save(commit=False)
            
            # Set the 'date_created' field to the current time
            instance.date_created = timezone.now()
            
            if commit:
                instance.save()
            return instance
       







from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth import authenticate
from .models import UserProfile

#çclass LoginForm(forms.Form):
#    username = forms.CharField()
#    password = forms.CharField(widget=forms.PasswordInput)
#
#    def get_user(self):
#        password = self.cleaned_data.get('password')
#        user = authenticate(username=username, password=password)  # Ensure authentication
#        if user is None:
#            raise forms.ValidationError("Invalid login credentials")
#        return user



class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    contact = forms.CharField(max_length=15)
    choose = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email', 'contact', 'choose', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            UserProfile.objects.create(user=user, contact=self.cleaned_data['contact'], choose=self.cleaned_data['choose'])
        return user



class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    
    

    
            
        
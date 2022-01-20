from django import forms
#from django.forms import widgets
from basic_app.models import UserProfileInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')



#class UserProfileInfoForm(forms.ModelForm):
#    portfolio = forms.URLField(required=False)
#    picture = forms.ImageField(required=False)

#    class Meta:
#        model = UserProfileInfo
#        exclude = ('user',)

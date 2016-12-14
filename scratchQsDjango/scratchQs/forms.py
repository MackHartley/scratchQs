from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
	)

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username','email','password']

# class LoginForm(AuthenticationForm):
# 	username = forms.CharField(label="Username", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
# 	password = forms.CharField(label="Password", max_length=30, widget=forms.PasswordInput)
# Tutorial: https://www.youtube.com/watch?v=Aqj8no2tb5c&t=186s
class UserLoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput) # One form much larger than the other. Can this be fixed?
	password = forms.CharField(widget=forms.PasswordInput)

	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")
		if username and password:
			user = authenticate(username=username, password=password)
			if not user:
				raise forms.ValidationError("This user does not exist")
			if not user.check_password(password):
				raise forms.ValidationError("Incorrect password")
			if not user.is_active:
				raise forms.ValidationError("This user is no longer active.")
			return super(UserLoginForm, self).clean(*args, **kwargs)
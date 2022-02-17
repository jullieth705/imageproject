from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import ImageResource

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(required=True, label="Usuario")

class ImageForm(forms.ModelForm):
    name = forms.CharField(required=True, max_length=100, label="Nombre de la imagen")
    source = forms.ImageField(required=True, label="Imagen")

    class Meta:
        model = ImageResource
        fields = ('source','name',)


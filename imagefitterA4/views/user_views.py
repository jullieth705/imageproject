from django.shortcuts import  render, redirect
from ..forms import NewUserForm, LoginUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import require_safe, require_http_methods

HOME_URL = 'imagefitterA4:home' 

@require_http_methods(['GET', 'POST'])
def register_request(request):
	if request.method == 'POST':
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, 'Registro exitoso.' )
			return redirect(HOME_URL)
		messages.error(request, 'Registro fallido.')
	form = NewUserForm()
	return render (request=request, template_name='./register.html', context={'register_form':form})

@require_http_methods(['GET', 'POST'])
def login_request(request):
	if request.method == 'POST':
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f'Has iniciado sesión como {username}.')
				URL = request.GET['next'] if 'next' in request.GET else HOME_URL
				return redirect(URL)
			else:
				messages.error(request,'Usuario o contraseña incorrectos.')
		else:
			messages.error(request,'Usuario o contraseña incorrectos.')
	form = LoginUserForm()
	return render(request=request, template_name='./login.html', context={'login_form':form})

@require_safe
def logout_request(request):
	logout(request)
	messages.info(request, 'Has cerrado sesión exitosamente.') 
	return redirect('imagefitterA4:login')
from django.shortcuts import  render, redirect
from .forms import NewUserForm, ImageForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from .models import ImageResource
from PIL import Image
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_safe, require_POST, require_GET

HOME_URL = 'imagefitterA4:home' 

@require_safe
@login_required
def home(request):
	return render(request=request, template_name='./home.html') 

@require_safe
@login_required
def galery(request):
	images = ImageResource.objects.filter(user=request.user)
	return render(request=request, template_name='./galery.html', context={'images':images}) 

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
				try:
					if request.GET['next']:
						return redirect(request.GET['next'])
				except Exception:
					return redirect(HOME_URL)
			else:
				messages.error(request,'Usuario o contraseña incorrectos.')
		else:
			messages.error(request,'Usuario o contraseña incorrectos.')
	form = AuthenticationForm()
	return render(request=request, template_name='./login.html', context={'login_form':form})

@require_safe
def logout_request(request):
	logout(request)
	messages.info(request, 'Has cerrado sesión exitosamente.') 
	return redirect(HOME_URL)

def fit_image(source):
	image = Image.open(source)
	height = image.height
	width = image.width

	dimensions_a4 = { 
		'vertical' :{'height' : 1123, 'width' : 796},
		'horizontal' : {'height' : 796, 'width' : 1123}
	}
	orientation = 'vertical' if (height >= width) else'horizontal'
	if (height > dimensions_a4[orientation]['height'] or width > dimensions_a4[orientation]['width']):
		image.thumbnail([dimensions_a4[orientation]['width'], dimensions_a4[orientation]['height']], Image.ANTIALIAS)	
	image.save(settings.MEDIA_URL[1:] + settings.IMAGE_URL + str(source))  
	source_details = { 
		'path' : settings.IMAGE_URL + str(source),
		'orientation': orientation,
		'dimensions': str(image.width)+ 'X' + str(image.height)}
	return source_details

@require_safe
@login_required
def upload(request):
	if request.method == 'POST':
		form = ImageForm(request.POST, request.FILES)
		if form.is_valid():
			temp_form = form.save(commit=False)
			source_details = fit_image(temp_form.source)
			temp_form.source = source_details['path']
			temp_form.orientation = source_details['orientation']
			temp_form.dimensions = source_details['dimensions']
			temp_form.user = request.user
			temp_form.save()
			image = ImageResource.objects.filter(user=request.user).last()
			return redirect('imagefitterA4:view', pk=image.pk)
		return redirect('imagefitterA4:upload')
	form = ImageForm()
	images = ImageResource.objects.filter(user=request.user)
	return render(request=request, template_name='./upload.html', context={'form':form, 'images':images}) 

@require_safe
@login_required
def view(request, pk):
	image = ImageResource.objects.filter(user=request.user).get(pk=pk)
	return render(request=request, template_name='./pageA4.html', context={'image':image})
   
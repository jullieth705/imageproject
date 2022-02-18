from django.shortcuts import  render, redirect
from ..forms import ImageForm
from django.contrib import messages
from ..models import ImageResource
from PIL import Image
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_safe, require_http_methods

@require_safe
@login_required
def galery(request):
	images = ImageResource.objects.filter(user=request.user)
	return render(request=request, template_name='./galery.html', context={'images':images}) 

def fit_image(source, name, number_file):
	image = Image.open(source)
	if image.format == "JPEG" or image.format == "JPG":
		height = image.height
		width = image.width
		dimensions_a4 = { 
			'vertical' :{'height' : 1123, 'width' : 796},
			'horizontal' : {'height' : 796, 'width' : 1123}
		}
		orientation = 'vertical' if (height >= width) else'horizontal'
		if (height > dimensions_a4[orientation]['height'] or width > dimensions_a4[orientation]['width']):
			image.thumbnail([dimensions_a4[orientation]['width'], dimensions_a4[orientation]['height']], Image.ANTIALIAS)	
		name = name if number_file == 0 else name + ' (' + str(number_file) + ')'
		filename = name + '.'+ image.format.lower()
		image.save(settings.MEDIA_URL[1:] + settings.IMAGE_URL + filename)  
		
		source_details = { 
			'path' : settings.IMAGE_URL + filename,
			'orientation': orientation,
			'dimensions': str(image.width)+ 'X' + str(image.height),
			'name': name}
	else:
		source_details = {'error' : f'El archivo se encuentra corrupto o tiene un formato invalido. Las extensiones permitidas son: jpeg, jpg.'}
	return source_details

@require_http_methods(['GET', 'POST'])
@login_required
def upload(request):
	if request.method == 'POST':
		form = ImageForm(request.POST, request.FILES)
		files = request.FILES.getlist('source')
		images = []
		if form.is_valid():
			temp_form = form.save(commit=False)
			number_file = 0
			for file in files:
				source_details = fit_image(file, temp_form.name, number_file)
				number_file += 1
				if 'error' in source_details:
					messages.error(request,source_details['error'])
				else:
					name = source_details['name']
					source = source_details['path']
					orientation = source_details['orientation']
					dimensions = source_details['dimensions']
					user = request.user
					ImageResource.objects.create(name = name, source=source, orientation=orientation, dimensions=dimensions, user = user)
					images.append(ImageResource.objects.filter(user=request.user).last())
			if len(images) == 1:	
				return redirect('imagefitterA4:view', pk=images[0].pk)
			elif len(images) > 1:
				return render(request=request, template_name='./galery_preview.html', context={'images':images})
		else:
			messages.error(request,'Los archivos ingresados deben ser de tipo imagen. Las extensiones permitidas son: jpeg, jpg.')
		return redirect('imagefitterA4:upload')
	form = ImageForm()
	images = ImageResource.objects.filter(user=request.user)
	return render(request=request, template_name='./upload.html', context={'form':form, 'images':images}) 

@require_safe
@login_required
def view(request, pk):
	image = ImageResource.objects.filter(user=request.user).get(pk=pk)
	return render(request=request, template_name='./page_a4.html', context={'image':image})
   
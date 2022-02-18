from django.shortcuts import  render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_safe

@require_safe
@login_required
def home(request):
	return render(request=request, template_name='./home.html') 

from django.urls import path
from . import views

app_name = 'imagefitterA4'

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/register/', views.register_request, name='register'),
    path('accounts/login/', views.login_request, name='login'),
    path('accounts/logout/', views.logout_request, name= 'logout'),
    path("upload", views.upload, name="upload"),
    path("galery", views.galery, name="galery"),
    path('images/<pk>/', views.view, name="view"),
]
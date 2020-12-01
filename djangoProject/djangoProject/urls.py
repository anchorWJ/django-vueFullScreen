"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path, include
from django.contrib import admin
from core import views
from django.views.generic.base import TemplateView

urlpatterns = (
    path('admin/', admin.site.urls),
    # connect with vue homepage
    #re_path(r'^$', TemplateView.as_view(template_name='index.html')),
    path('api/', include('core.urls')),
    #path('goAbroad/', views.goAbroad),
    #path('sumValue/', views.sumCheck)
)

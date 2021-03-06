"""weddingupload URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

from upload import views as upload_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view(), name='home'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('thanks/', views.ThanksPage.as_view(), name='thanks'),
    path('upload/', upload_views.DocumentCreateView.as_view(), name='upload'),
    path('photos/', include('photos.urls', namespace='photos')),
]

# Admin Site Config
admin.sites.AdminSite.site_header = 'Wedding Administration Zone'
admin.sites.AdminSite.site_title = 'WeddingUpload Admin'
admin.sites.AdminSite.index_title = 'Guests and Photos Administration'

"""veksorHUB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from main_hub import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),

    path('projects/', views.projects),
    path('projects/<slug:url>', views.project),
    path('projects/<slug:url>/<file>', views.file_projects, name="file_projects"),


    path('cloud/', views.cloud, name='cloud'),
    path('cloud/<url>/', views.files, name="files"),
    path('cloud/<url>/<file>', views.file_download, name="file_download"),
    path('upload/', views.model_form_upload, name='upload'),
    path('delete_folder/<folder>', views.delete_folder, name='delete_folder'),
    path('delete_file/<int:pk>', views.delete_file, name='delete_file'),

    path('short/', views.short_url, name='short_url'),
    path('short/<name>', views.short_redirect, name='short_redirect'),
    path('short/sucess/<name>', views.short_sucessful, name='short_sucessful'),
    path('delete_url/', views.delete_url, name='short_delete'),
    path('contact/', views.contact, name='contact'),

    path('admin/', admin.site.urls),

    path('vekflix/', views.vekflix_index, name='vekflix'),
    path('vekflix/<slug:lien>', views.vekflix_show, name='vekflix_show'),
    path('vekflix/<slug:lien>/<slug:type>/<file>', views.file_vekflix, name="file_vekflix"),
    path('vekflix/sard/', views.ytb_vekflix, name="ytb_vekflix"),

    path('ytb/', views.youtube_home, name='ytb'),
    path('ytb/delete', views.youtube_delete, name='ytbdelete'),

    path('bus/', views.bus_home, name='bus_home'),
    path('bus/<file>', views.file_bus, name='bus_file'),
    path('bus/<stopa>/<stopr>/', views.bus_link, name='bus_link'),
    path('robert/', views.robert, name='robert'),
    path('isn/', views.p5js),
    path('isn/<str:number>', views.exo),
    path('QR_code/', views.qrcode,name='qrcode'),
    path('steganography/', views.steganography,name='steganography'),
    path('steganography/decrypt/', views.steganographydecrypt,name='steganography_decrypt'),
    path('face_recognition/', views.face_recognition,name='face_recognition'),
    path('thispersondoesnotexist/', views.random_person,name='random_person'),
    path('bac_maths/', views.mathtraining,name='math'),
    path('tracking/', include('tracking.urls')),


]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
    path('', views.home, name='home'),
    path('projets/',views.projects),
    path('projet/<slug:url>',views.project),
    
    path('admin/?next=/delete_file/<int:pk>', views.delete_file),
    path('cloud/', views.cloud, name='cloud'),
    path('cloud/<url>/', views.files, name="files"),
    path('upload/', views.model_form_upload, name='upload'),
    path('delete_folder/<folder>', views.delete_folder, name='delete_folder'),
    path('delete_file/<int:pk>', views.delete_file, name='delete_file'),
    path('short/', views.short_url, name='short_url'),
    path('short/<name>', views.short_redirect, name='short_redirect'),
    path('short/sucess/<name>', views.short_sucessful, name='short_sucessful'),
    path('delete_url/', views.delete_url, name='short_delete'),
    path('contact/', views.contact, name='contact'),
    
    path('admin/', admin.site.urls),
    path('vekflix/', views.vekflix_index, name='vekflix'),
    path('vekflix/<slug:lien>', views.vekflix_show, name='vekflix_show'),
"""
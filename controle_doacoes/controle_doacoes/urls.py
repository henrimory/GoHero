"""controle_doacoes URL Configuration

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
from django.contrib import admin
from django.urls import path
from doacoes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', views.main , name="url_main"),
    path('', views.inicio , name="url_ini"),
    path('login/', views.login , name="url_log"),
    path('cadastroOng/', views.cadastroOng , name="url_cadOng"),
    path('cadastroUser/', views.cadastroUser , name="url_cadUser"),
    path('perfil/', views.perfil , name="url_perfil"),
    path('infos/', views.infos , name="url_infos"),
    path('favoritos/', views.favoritos , name="url_favoritos"),
]

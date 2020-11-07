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
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name="url_home"),
    path('', views.inicio, name="url_ini"),
    path('login/', views.login, name="url_login"),
    path('logout/', views.login, name="url_logout"),
    path('cadastroOng/', views.cadastroOng, name="url_cadOng"),
    path('cadastroUser/', views.cadastroUser, name="url_cadUser"),
    path('cadastroUser/', views.contatos, name='url_cadUser'),
    path('cadastroEnde/', views.cadastroEnde, name="url_cadEnde"),
    path('cadastroEndeOng/', views.cadastroEndeOng, name="url_cadEndOng"),
    path('perfil/', views.perfil, name="url_perfil"),
    path('infos/<int:pk>', views.infos,name="url_infos" ),
    path('favoritos/', views.favoritos, name="url_favoritos"),
    path('deletePostOng/<int:pk>',views.deletePostOng,name="url_deletePostOng"),
    path('deletePostDoador/<int:pk>',views.deletePostDoador,name="url_deletePostDoador"),
    path('editPostDoador/<int:pk>', views.editPostDoador, name="url_editPostDoador"),
    path('editPostOng/<int:pk>', views.editPostOng, name="url_editPostOng"),
    path('newPost/<int:pk>', views.newPost, name="url_newPost"),
    path('newPostOng/<int:pk>', views.newPostOng, name="url_newPostOng"),
    path('home/postOng/', views.homePostOng, name='url_homePostOng'),
    path('home/postDoador/', views.homePostDoador, name='url_homePostDoador'),
    path('perfil/<str:pk>', views.visitPerfil, name='url_visitPerfil'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

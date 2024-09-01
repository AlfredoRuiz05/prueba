from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name= "usuarios"
urlpatterns = [

    path('registrarse/', views.registrarse, name='registrarse'),
]
    
    #path('registrarse/', views.registrarse, name='registrarse'),
    #path('perfil/', views.ver_perfil, name='ver_perfil'),
    #path('editar/', views.editar_perfil, name='editar_perfil'),
    #path('favoritos/', views.listar_favoritos, name='listar_favoritos'),
    #path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
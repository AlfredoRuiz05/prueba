from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.iniciar_sesion, name='iniciar_sesion'),
    path('productos/', include('app.productos.urls')),
    path('usuarios/', include('app.usuarios.urls')),
] 

    #path('categorias/', include('apps.categorias.urls')),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #path('registrarme/',views.registrarme, name= 'registrarme'),
    #path('login/', views.login, name='login'),
from django.shortcuts import render, redirect
from app.productos.models import Producto
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import EditarPerfilForm, FormularioRegistroUsuario
from django.contrib.admin.views.decorators import user_passes_test
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model 
from .models import Usuario

User = get_user_model()




# usuarios no autenticados
"""def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/listar_productos.html', {'productos': productos})

def ver_detalle_producto(request, producto_id):
    producto = Producto.objects.get(pk=producto_id)
    return render(request, 'productos/detalle_producto.html', {'producto': producto})"""
def registrarse(request):
    if request.method == 'POST':
        form = FormularioRegistroUsuario(request.POST)
        if form.is_valid():
            form.save()  # Guardar el nuevo usuario
            messages.success(request, 'Cuenta creada con éxito. Ahora puedes iniciar sesión.')
            return redirect('iniciar_sesion')  # Redirige a la página de inicio de sesión
    else:
        form = FormularioRegistroUsuario()
    return render(request, 'usuarios/registrarse.html', {'form': form})

#def registrarse(request):
 #   if request.method == 'POST':
 #       form = FormularioRegistroUsuario(request.POST)
 #       if form.is_valid():
 #           form.save()
#            return redirect('login')  # Redirige a la página de inicio o a otra página después del registro
 #   else:
#        form = FormularioRegistroUsuario()
#    return render(request, 'usuarios/registrarme.html', {'form': form})


#usuarios autenticados
#@login_required
def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Cambia a 'home' o a otra URL relevante
        else:
            messages.error(request, 'Credenciales inválidas. Por favor, inténtalo de nuevo.')
    return render(request, 'usuarios/login.html')


#@login_required
#def ver_perfil(request):
#    # Obtener el usuario autenticado
#    usuario = request.user
#    return render(request, 'usuarios/ver_perfil.html', {'usuario': usuario})

#@login_required
#def editar_perfil(request):
 #   if request.method == 'POST':
 #       form = EditarPerfilForm(request.POST, instance=request.user)
 #       if form.is_valid():
 #           form.save()
 #           messages.success(request, 'Tu perfil ha sido actualizado exitosamente.')
 #           return redirect('usuarios:ver_perfil')
 #   else:
 #       form = EditarPerfilForm(instance=request.user)
 #   return render(request, 'usuarios/editar_perfil.html', {'form': form})

#usuarios administradores
def es_admin(user):
    return user.is_authenticated and user.is_staff



# Decorador para permitir solo a los administradores acceder a esta vista
@user_passes_test(lambda u: u.is_superuser)
def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/listar_usuarios.html', {'usuarios': usuarios})


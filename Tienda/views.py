from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth import logout
#from apps.usuarios.models import Usuario
from app.productos.models import Producto

#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def home(request):
    productos = Producto.objects.all()
    buscador = request.GET.get('buscador', '')
    if buscador:
        productos = productos.filter(nombre__icontains=buscador)
    return render(request, 'base.html', {'productos': productos, 'buscador': buscador})

def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Inicio de sesión exitoso.')
            return redirect('home')  # Redirige a la vista que renderiza base.html
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')

    return render(request, 'login.html')
#def login(request):
   # if request.method == 'POST':
  #      username = request.POST['username']
   #     password = request.POST['password']
   #     user = authenticate(request, username=username, password=password)
  #      if user is not None:
  #          auth_login(request, user)
 #           return redirect('pagina_principal')
 #       else:
 #           messages.error(request, 'Usuario y/o contraseña incorrecta.')
 #   return render(request, 'login.html')





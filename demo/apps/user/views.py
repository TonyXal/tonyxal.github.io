from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from .models import User
from apps.user.forms import LoginForm, RegisterForm
from apps.empresa.models import Empresa, Depto


# Index view
# @csrf_exempt
def index(request):
    '''Página Index para usuarios autentificados'''
    if request.user.is_authenticated:
        # Verifica si ya se creó la empresa
        if Empresa.objects.first() is not None:
            # La empresa ya existe
            empresa = Empresa.objects.first()
            usr = request.user.id
            user = User.objects.get(pk=usr)
            if user.empleado.exists():
                # El usuario ya cuenta con departamento
                depto = user.empleado.values_list().get()[1]
                if depto == 'Gerencia':
                    # Nivel 'Gerente'.
                    nivel = 1
                else:
                    # Nivel 'Empleado'.
                    nivel = 2
            else:
                # El usuario NO cuenta con departamento
                nivel = 3
                depto = None

            return render(request, 'index.html', {
                'title':'Empleado',
                'user':user,
                'empresa':empresa,
                'nivel':nivel,
                'depto':depto,
            })
        else:
            # Aún no se crea la empresa, puede crear una nueva empresa
            return HttpResponseRedirect(reverse("empresa:nuevaempresa"))
    else:
        # User must to sign in.
        return HttpResponseRedirect(reverse("user:login"))


# Log in view
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            # Attempt to sign user in
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            # try:
            if user is None:
                return render(request, "user/login.html", {
                    'title':'Login',
                    'message':"username y/o contraseña invalido.",
                    'form':form,
                })
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
            # except AttributeError as e:
        else:
            return render(request, "user/login.html", {
                'title':'Login',
                'message':"Error encontrado.",
                'form':form,
            })
    else:
        return render(request, "user/login.html", {
            'title':'Login',
            'form':LoginForm(),
        })



# @csrf_exempt
# @login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


# Register View
def register(request):
    # Registering new users
    if request.method == "POST":
        form = RegisterForm(request.POST)
        # Verifying form
        if form.is_valid():
            # Ensures password matches confirmation
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            iniciales = form.cleaned_data['iniciales']
            password = form.cleaned_data['password']
            confirm = form.cleaned_data['confirm']
            if password != confirm:
                return render(request, "user/register.html", {
                    'title':'Register',
                    'form':form,
                    "message": "Las contraseñas deben coincidir.",
                })
            # Crea el nuevo usuario y lo autentifica
            user = User.objects.create_user(username=username, email=email, iniciales=iniciales, password=password)
            user = authenticate(request, username=username, password=password)
            if user is None:
                return render(request, "user/register.html", {
                    'title':'Register',
                    'message': 'No se pudo autenticar el nuevo usuario tras crearlo. Revisa "AUTH_USER_MODEL" en "settings.py".',
                    'form':form,
                })
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'user/register.html', {
                'title':'Register',
                'message': 'Verifique los datos ingresados.',
                'form': form,
            })
    else:
        return render(request, "user/register.html", {
            'title':'Register',
            'form':RegisterForm(),
        })

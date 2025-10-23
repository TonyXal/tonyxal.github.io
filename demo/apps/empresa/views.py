from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from apps.user.models import User
from .models import Empresa, Depto
from .forms import NuevaEmpresaForm, AsignaDeptoForm


@login_required
# @csrf_exempt
def nuevaempresa(request):
    '''Registro de la nueva empresa.'''
    if request.method == 'POST':
        form1 = NuevaEmpresaForm(request.POST) 
        if form1.is_valid():
            # form1 es válido
            if Empresa.objects.first() is None:
                form2 = AsignaDeptoForm(request.POST)
                if form2.is_valid():
                    # form2 es válido
                    nombreEmp = form1.cleaned_data['nombreEmp']
                    usr = request.user
                    user = User.objects.get(pk=usr.id)
                    desc = form1.cleaned_data['descripcion']
                    nombreDepto = form2.cleaned_data['nombreDepto']

                    # Creates the company, Management department and manager
                    empresa = Empresa.objects.create(nombreEmp=nombreEmp, descripcion=desc)
                    depart = Depto.objects.create(nombreDepto=nombreDepto)
                    depart.empleados.add(user.id)
                    empresa.deptos.add(depart)
                    return render(request, 'index.html', {
                        'title':'Nueva Empresa',
                        'empresa':empresa,
                        'empleado':user,
                        'stt':'open',
                    })
            else:
                return render(request, 'empresa/crear.html', {
                    'title':'Nueva Empresa',
                    'message3':'La empresa ya fue creada. No puedes creear otra',
                })
        else:
            return render(request, 'empresa/crear.html', {
                'title':'Nueva Empresa',
                'message3':'Valor invalido del formulario. Por favor intente de nuevo.',
                'form1':form1,
            })
    else:
        if Empresa.objects.first():
            exists = True
            form1 = None
            form2 = None
            empresa = Empresa.objects.first()
        else:
            exists = False
            form1 = NuevaEmpresaForm()
            form2 = AsignaDeptoForm()
            empresa = None
        return render(request, 'empresa/crear.html', {
            'title':'Nueva Empresa',
            'exists':exists,
            'form1':form1,
            'form2':form2,
            'empresa':empresa,
        })


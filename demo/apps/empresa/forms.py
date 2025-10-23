from django import forms
from apps.user.models import User
from apps.empresa.models import Empresa, Depto


class NuevaEmpresaForm(forms.ModelForm):
    '''Registro de nueva empresa'''
    class Meta:
        model = Empresa
        fields = ['nombreEmp', 'descripcion']
        labels = {
            'nombreEmp': 'Nombre de la Empresa',
            'descripcion': 'Descripción de la Empresa',
        }
        widgets = {
            'nombreEmp':forms.TextInput(attrs={'class':'form-control col-md-9 mb-2', 
                                               'placeholder':'Nombre Empresa', 'id':'empID'}),
            'descripcion':forms.TextInput(attrs={'class':'form-control col-md-9 mb-2', 
                                                 'placeholder':'Descripción', 'id':'descID'}),
        }


class AsignaDeptoForm(forms.ModelForm):
    '''Asks for a new department'''
    class Meta:
        model = Depto
        fields = ['nombreDepto']
        labels = {'nombreDepto': 'Nuevo Departamento'}
        widgets = {
            'nombreDepto':forms.TextInput(attrs={'class':'form-control col-md-7 mb-2', 'id':'deptID',
                                                'placeholder':'Nombre del nuevo Departamento'}),
        }



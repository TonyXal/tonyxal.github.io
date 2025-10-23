from django import forms
from apps.user.models import User


# Registration form
class RegisterForm(forms.ModelForm):
    '''Registro de nuevos Usuarios.
        
        Campos Obligatorios:
        - username: Nombre del usuario.
        - email: Correo electrónico.
        - Iniciales: Iniciales del usuario.
        - password: Contraseña.
        - confirm: Confirmación de la contraseña.
    '''

    password = forms.CharField(label='Contraseña', required=True, widget=forms.PasswordInput(attrs={
        'id':'pwd1',
        'class':'form-control col-md-5 mb-2', 
        'placeholder':'Contraseña'})
        )

    confirm = forms.CharField(label='Confirma la contraseña', required=True, widget=forms.PasswordInput(attrs={
        'id':'pwd2',
        'class':'form-control col-md-5 mb-2',
        'placeholder':'Confirma la contraseña'})
        )

    class Meta:
        model = User
        fields = ['username', 'email', 'iniciales']
        labels = {
            'username':'Nombre de Usuario',
            'email':'Correo Electrónico',
            'iniciales':'Tus Iniciales',
            'password':'Contraseña',
        }
        widgets = {
            'username':forms.TextInput(attrs={'id':'usrID',
                                              'class':'form-control col-md-5 mb-2', 
                                              'placeholder':'Usuario'}),
            'email':forms.EmailInput(attrs={'id':'usrEmail',
                                            'class':'form-control col-md-5 mb-2', 
                                            'placeholder':'Correo Electrónico', }),
            'iniciales':forms.TextInput(attrs={'id':'usrIniciales',
                                               'class':'form-control col-md-5 mb-2', 
                                               'placeholder':'Tus Iniciales',
                                               'maxlength':'4'}),
        }


# Login form
class LoginForm(forms.Form):
    '''Formulario para iniciar sesión.'''

    username = forms.CharField(label='Username', required=True, widget=forms.TextInput(attrs={
        'class':'form-control col-md-4 mb-2', 'placeholder':'Username'}))
    password = forms.CharField(label='Contraseña', required=True, widget=forms.PasswordInput(attrs={
        'id':'pwd1', 'class':'form-control col-md-4 mb-2', 'placeholder':'Contraseña'}))


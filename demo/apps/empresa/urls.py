from django.urls import path
from apps.empresa import views

app_name = 'empresa'
urlpatterns = [
    path('nuevaempresa', views.nuevaempresa, name='nuevaempresa'),
    
]
               
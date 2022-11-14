from django import forms
from blog.models import Post

class PostForm(forms.ModelForm): #creamos una clase que hereda información de un modelo
    class Meta: # se define la clase meta 
        model = Post # el modelo con el que se quiere vincular
        fields = ['titulo', 'resumen', 'contenido', 'autor']


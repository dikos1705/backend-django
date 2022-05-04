from turtle import width

from matplotlib import widgets
from .models import City
from django.forms import ModelForm,TextInput



class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets={'name' : TextInput(attrs={
        'class' :'form-control',
        'name':'city',
        'id':'city',
        'placeholder':"Введите город",
        })}
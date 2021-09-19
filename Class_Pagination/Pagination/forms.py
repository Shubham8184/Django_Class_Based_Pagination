from django import forms

from .models import Laptop




class Laptopform(forms.ModelForm):
    class Meta:
        model=Laptop
        fields='__all__'
        labels={
            'laptopname':'Laptop Name',
            'laptopcompany':'Laptop Company',
            'laptopram':'Laptop RAM',
            'laptoprom':'Laptop ROM',
            'laptopprice':'Laptop Price',
            'laptopprocessor':'Laptop Processor'
        }
        widgets={
            'laptopname':forms.TextInput(attrs={'placeholder':'Enter Laptop Name'}),
            'laptopcompany':forms.TextInput(attrs={'placeholder':'Enter Laptop Company name'}),
            'laptopram':forms.TextInput(attrs={'placeholder':'Enter Laptop RAM'}),
            'laptoprom':forms.TextInput(attrs={'placeholder':'Enter Laptop ROM'}),
            'laptopprice':forms.TextInput(attrs={'placeholder':'Enter Laptop Price'}),
            'laptopprocessor':forms.TextInput(attrs={'placeholder':'Enter Laptop Processor'}),
        }
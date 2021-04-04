from django import forms
from .models import User

class StudentRegistation(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name' ,'email' ,'passward']

        widgets = {

            'name':forms.TextInput(attrs={'class':'form-control' }),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'passward':forms.PasswordInput(attrs={'class':'form-control'}),
        }





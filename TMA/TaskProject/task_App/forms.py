from django.forms import ModelForm
from .models import *

class Main_Form(ModelForm):
    
    class Meta:
        model = Mainclass
        fields ='__all__'
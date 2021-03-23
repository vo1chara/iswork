from .models import Domen
from django import forms

class DomenForm(forms.ModelForm):
    class Meta:
        model = Domen 
        fields = ('name', 'webserver')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
    
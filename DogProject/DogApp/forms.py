from django.forms import ModelForm
from .models import DogModel

class DogForm(ModelForm):
    class Meta:
        model = DogModel
        fields = '__all__'

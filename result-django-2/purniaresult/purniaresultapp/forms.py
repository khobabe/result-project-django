from django.forms import ModelForm
from .models import Result

class InsertFormResult(ModelForm):
    class Meta:
        model = Result
        fields = '__all__'
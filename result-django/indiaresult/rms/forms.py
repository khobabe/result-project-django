from django.forms import ModelForm #import "ModelForm" to inherit it.
from .models import Result


# after just defining the following class,apke model me jitna coloumn hai wo is class se automatically HTML ka form ban jayega:
class InsertResultForm(ModelForm): #inherit, => Model se banana hai form is liye "ModelForm" ko inherit kar rahe hain.
    class Meta: #it is called inner class(class within class)
        model = Result
        fields = '__all__'
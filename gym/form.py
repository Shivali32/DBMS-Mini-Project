from django import forms  
from gym.models import member, trainer, facility
  
class memberForm(forms.ModelForm):  
    class Meta:  
        model = member
        fields = ("__all__")

class trainerForm(forms.ModelForm):  
    class Meta:  
        model = trainer
        fields = ("__all__")


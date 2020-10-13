from django import forms  
from gym.models import member, trainer, facility
  
class memberForm(forms.ModelForm):  
    class Meta:  
        model = member
        fields = ("m_name", "m_age", "m_phno")

class trainerForm(forms.ModelForm):  
    class Meta:  
        model = trainer
        fields = ("t_name", "t_age", "t_phno")
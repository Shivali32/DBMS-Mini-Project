from django import forms  
from gym.models import member, trainer, facility
  
class memberForm(forms.ModelForm):  
    class Meta:  
        model = member
        fields = ("__all__")
        labels = {
            "m_name" : "Member Name",
            "m_age"  : "Member Age",
            "m_phno" : "Phone Number",
            "m_time"  : "Gym Timing",
            "m_years" : "Years Training",
            "m_tid" : "Trainer Available",
            "m_fid" : "Facility Available",
                }        


class trainerForm(forms.ModelForm):  
    class Meta:  
        model = trainer
        fields = ("__all__")
        labels = {
            "t_name" : "Trainer Name",
            "t_age"  : "Trainer Age",
            "t_phno" : "Phone Number",
            "t_hours"  : "Working Hours",
            "t_salary" : "Expected Salary",
            "t_fid" : "Avail Facility",
                }

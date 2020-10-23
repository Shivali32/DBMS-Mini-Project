from django import forms  
from gym.models import member, trainer, facility


time_choices = [ ('4-5','4-5'), ('5-6','5-6'), ('6-7','6-7'), ('7-8','7-8'), ('8-9','8-9'), ]
salary_choices = [ ('15000','15000'), ('20000','20000'), ('25000','25000'), ('30000','30000'), ]
  
class memberForm(forms.ModelForm):  
    m_time = forms.CharField(label = 'Gym Timing', widget = forms.RadioSelect(choices = time_choices))
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
    t_salary = forms.CharField(label = 'Expected Salary', widget = forms.RadioSelect(choices = salary_choices))
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



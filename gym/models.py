from django.db import models

# Create your models here.


#from __future__ import unicode_literals  
  
class facility(models.Model):  
    f_name  = models.CharField(max_length = 100, null = False)
    f_cost  = models.CharField(max_length = 20) 
    f_timing = models.CharField(max_length = 20)
    class Meta:  
        db_table = "facility"          
    def __str__(self):
        return self.f_name

class trainer(models.Model):  
    t_name  = models.CharField(max_length = 100, null = False)
    t_age  = models.CharField(max_length = 20)
    t_phno = models.CharField(max_length = 20)
    t_hours  = models.CharField(max_length = 20)
    t_salary = models.CharField(max_length = 20)
    t_fid = models.ForeignKey(facility, on_delete=models.CASCADE)
    class Meta:  
        db_table = "trainer"          
    def __str__(self):
        return self.t_name

class member(models.Model):  
    m_name  = models.CharField(max_length = 100, null = False,)
    m_age  = models.CharField(max_length = 20)
    m_phno = models.CharField(max_length = 20)
    m_time  = models.CharField(max_length = 20)
    m_years = models.CharField(max_length = 20)
    m_tid  = models.ForeignKey(trainer, on_delete=models.CASCADE)
    m_fid  = models.ForeignKey(facility, on_delete=models.CASCADE)
    class Meta:  
        db_table = "member"          
    def __str__(self):
        return self.m_name


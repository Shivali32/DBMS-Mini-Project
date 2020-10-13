from django.contrib import admin

# Register your models here.


from gym.models import member, trainer, facility
admin.site.register(member)
admin.site.register(trainer)
admin.site.register(facility)
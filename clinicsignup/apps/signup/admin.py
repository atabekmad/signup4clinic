from django.contrib import admin

from .models import *


class AppointmentInline(admin.StackedInline):
    model = Appointment


class DoctorAdmin(admin.ModelAdmin):
    fields = ['doctor_full_name']
    inlines = [AppointmentInline]


    

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Appointment)




# Register your models here.



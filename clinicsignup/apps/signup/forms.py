from django import forms
from django.forms import ModelForm
from .models import Doctor, Appointment


class SignupForm(ModelForm):

    class Meta:
        model = Appointment
        fields = ['patient_first_name','patient_last_name','patient_middle_name','doctor','appointment_date','appointment_time']


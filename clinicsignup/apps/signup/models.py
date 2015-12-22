from django.db import models


class Doctor(models.Model):

    doctor_full_name = models.CharField(max_length=200, default='Xren Dmitriy Nikolaevich')

    def __str__(self):
        return self.doctor_full_name


class Appointment(models.Model):

    patient_first_name = models.CharField(max_length=200)
    patient_last_name = models.CharField(max_length=200)
    patient_middle_name = models.CharField(max_length=200)
    doctor = models.ForeignKey(Doctor)
    appointment_date = models.DateField("Appointment's date", blank=True, null=True) 
    appointment_time = models.TimeField("Appointment's time", blank=True, null=True)

    def patient_full_name(self):
        # why can't I make a field containing a full name??
        return self.patient_last_name + ' ' + self.patient_first_name + ' ' + self.patient_middle_name        

    def __str__(self):
        # gotta research the format  
        return str(self.id) + '. ' + str(self.appointment_date) + ' ' + self.patient_full_name()

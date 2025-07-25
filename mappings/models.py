from django.db import models
from patients.models import Patient
from doctors.models import Doctor

class PatientDoctorMapping(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    assigned_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.name} ↔ {self.doctor.name}"

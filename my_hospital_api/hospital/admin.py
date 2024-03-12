from django.contrib import admin
from .models import Hospital, Service, Patient, Doctor, Driver, HospitalDoctor

# Register your models here.
admin.site.register(Hospital)
admin.site.register(Service)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Driver)
admin.site.register(HospitalDoctor)

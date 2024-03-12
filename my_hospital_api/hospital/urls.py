from django.urls import path
from rest_framework import routers
from .views import HospitalViewSet, ServiceViewSet, PatientViewSet, DoctorViewSet, DriverViewSet, HospitalDoctorViewSet

router = routers.DefaultRouter()
router.register(r'hospitals', HospitalViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'doctors', DoctorViewSet)
router.register(r'drivers', DriverViewSet)
router.register(r'hospital-doctors', HospitalDoctorViewSet)

urlpatterns = router.urls

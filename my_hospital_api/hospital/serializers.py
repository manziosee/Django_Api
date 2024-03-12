from rest_framework import serializers
from .models import Patient, Doctor, Hospital, Service, Driver, HospitalDoctor
from .permissions import IsAdminOrReadOnly

class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        # Add permission classes
        permission_classes = [IsAdminOrReadOnly]

    def validate_national_id(self, value):
        if len(value) != 16:
            raise serializers.ValidationError('National ID must be 16 digits.')
        return value

class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
        permission_classes = [IsAdminOrReadOnly]

    def validate_national_id(self, value):
        if len(value) != 16:
            raise serializers.ValidationError('National ID must be 16 digits.')
        return value

class HospitalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'
        permission_classes = [IsAdminOrReadOnly]

class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
        permission_classes = [IsAdminOrReadOnly]

class DriverSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'
        permission_classes = [IsAdminOrReadOnly]

    def validate_plate_number(self, value):
        if len(value) != 7:
            raise serializers.ValidationError('Plate number must be 7 characters.')
        return value

class HospitalDoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HospitalDoctor
        fields = '__all__'
        permission_classes = [IsAdminOrReadOnly]

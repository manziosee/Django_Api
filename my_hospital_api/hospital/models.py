from django.core.validators import RegexValidator
from django.db import models
from django.utils.text import slugify

def validate_national_id(value):
    if len(value) != 16:
        raise ValidationError('National ID must be 16 digits.')

def validate_plate_number(value):
    if len(value) != 7:
        raise ValidationError('Plate number must be 7 characters.')

class Hospital(models.Model):
    H_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=10)
    location_name = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Service(models.Model):
    S_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Patient(models.Model):
    U_id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    national_id = models.CharField(max_length=16, validators=[validate_national_id])
    password = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.fullname)
        super().save(*args, **kwargs)

class Doctor(models.Model):
    D_id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    national_id = models.CharField(max_length=16, validators=[validate_national_id])
    password = models.CharField(max_length=100)
    S_id = models.ForeignKey('Service', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.fullname)
        super().save(*args, **kwargs)

class Driver(models.Model):
    driver_id = models.AutoField(primary_key=True)
    names = models.CharField(max_length=100)
    driving_license = models.CharField(max_length=16)
    plate_number = models.CharField(max_length=7, validators=[validate_plate_number])
    phone_number = models.CharField(max_length=15)
    H_id = models.ForeignKey('Hospital', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.names)
        super().save(*args, **kwargs)

class HospitalDoctor(models.Model):
    Id = models.AutoField(primary_key=True)
    H_id = models.ForeignKey('Hospital', on_delete=models.CASCADE)
    D_id = models.ForeignKey('Doctor', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.H_id.name}-{self.D_id.fullname}")
        super().save(*args, **kwargs)

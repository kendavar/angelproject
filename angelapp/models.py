from django.db import models
from django.core.validators import URLValidator

# Create your models here.


class angeltable(models.Model):
    confirmPassword = models.TextField(max_length=100, null=True, blank=True)
    created_Date = models.DateTimeField(null=True, blank=True)
    description = models.TextField(max_length=10000, null=True, blank=True)
    deviceToken = models.TextField(max_length=1000, null=True, blank=True)
    email = models.EmailField(
        max_length=70, null=True, blank=True, unique=True)
    firstname = models.TextField(max_length=100, null=True, blank=True)
    gender = models.TextField(max_length=100, null=True, blank=True)
    firebase_id = models.TextField(max_length=500, null=True, blank=True)
    lastName = models.TextField(max_length=100, null=True, blank=True)
    password = models.TextField(max_length=100, null=True, blank=True)
    profilePic = models.TextField(models.TextField(
        validators=[URLValidator()]), null=True, blank=True)
    username = models.TextField(max_length=100, null=True, blank=True)


class theripsttable(models.Model):
    created_Date = models.DateTimeField(null=True, blank=True)
    description = models.TextField(max_length=10000, null=True, blank=True)
    deviceToken = models.TextField(max_length=1000, null=True, blank=True)
    email = models.EmailField(
        max_length=70, null=True, blank=True, unique=True)
    firstname = models.TextField(max_length=100, null=True, blank=True)
    gender = models.TextField(max_length=100, null=True, blank=True)
    firebase_id = models.TextField(max_length=500, null=True, blank=True)
    lastName = models.TextField(max_length=100, null=True, blank=True)
    profession = models.TextField(max_length=10000, null=True, blank=True)
    profilePic = models.TextField(models.TextField(
        validators=[URLValidator()]), null=True, blank=True)
    userId = models.TextField(max_length=1000, null=True, blank=True)
    username = models.TextField(max_length=100, null=True, blank=True)


class question_set(models.Model):
    expectation = models.TextField(max_length=500, null=True, blank=True)
    firebase_id = models.TextField(max_length=500, null=True, blank=True)
    interaction = models.TextField(max_length=100, null=True, blank=True)
    isConsulted = models.TextField(max_length=100, null=True, blank=True)
    issue = models.TextField(max_length=500, null=True, blank=True)



class fcm_info(models.Model):
    fcm_token = models.CharField(max_length=400)

    def __str__(self):
    	return self.fcm_token

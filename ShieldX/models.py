from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/UserProfile/',
                              default='C:/Users/Abhishek/OneDrive/Desktop/Themes/djangopro/static/img/blankUser.png')

    def __str__(self):
        return self.user.username


class UserRelatives(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    userRelativeFirstName = models.CharField(max_length=20)
    userRelativeLastName = models.CharField(max_length=20)
    userRelativeNumber = models.CharField(max_length=20)
    userRelativeEmail = models.CharField(max_length=20)
    userRelativeImage = models.ImageField(upload_to="img/relatives")

    def __str__(self):
        return self.userRelativeFirstName


class CarRegistration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    carHolderName = models.CharField(max_length=20)
    carModel = models.CharField(max_length=20)
    carMobileNumber = models.CharField(max_length=20)
    carMobileEmail = models.CharField(max_length=20)

    def __str__(self):
        return self.carHolderName

from django.db import models

# Create your models here.

# hier heb ik een model gebruikersLogin gemaakt
# waarbij ik hem een login, password, email, role en superUser
# gegeven heb 
class GebruikersLogin(models.Model):
    login = models.CharField(max_length=30),
    password = models.CharField(max_length=20),
    email = models.EmailField(max_length=50),
    role = models.CharField(max_length=12),
    superUser = models.BooleanField()



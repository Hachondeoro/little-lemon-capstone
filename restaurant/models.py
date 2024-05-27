from django.db import models
from datetime import datetime

#Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(default = 1)
    booking_date = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.name
    
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    inventory = models.IntegerField(default = 0)
    
    def __str__(self):
        return f'{self.title} : {str(self.price)}'

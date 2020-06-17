from django.db import models

# Create your models here.

class ContactList(models.Model):
    slno = models.AutoField(primary_key = True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    description = models.TextField()
    date_up_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message from '+ self.name
    
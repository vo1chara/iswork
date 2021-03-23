from django.db import models

# Create your models here.
class Domen(models.Model):
    WEBSERVER = (
        (1, "Apache"),
        (2, "Nginx"),
    )
    name = models.CharField(max_length=200, verbose_name='Host name')
    webserver = models.IntegerField(choices=WEBSERVER, verbose_name='Webserver')
    
    def __str__(self):
        return self.name

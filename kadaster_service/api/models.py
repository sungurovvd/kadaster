from django.db import models

class RequestHistory(models.Model):
    cadastre_number = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    response = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cadastre_number}"
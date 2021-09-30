from django.db import models

# Create your models here.
class Medicine(models.Model):
    med_name= models.CharField(max_length=100)
    manufacturer= models.CharField(max_length=100)
    price=models.IntegerField()

    def __str__(self):
        return self.med_name

class Prescription(models.Model):
    date=models.DateField()
    med_name=models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity=models.IntegerField()
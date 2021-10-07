from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User,null=True,blank=False,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True)
    age = models.CharField(max_length=150,null=True)
    phonenumber = PhoneNumberField(null=True)
    email = models.EmailField(max_length=200,null=True)
    address = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# class Medicines(models.Model):
#     med_name = models.CharField(max_length=200,null=True)
#     manufacturer = models.CharField(max_length=200,null=True)
#     price = models.IntegerField(null=True)

#     def __str__(self):
#         return self.med_name

class Medicine(models.Model):
    med_name = models.CharField(("Medicine Name"),max_length=200,null=False,default="Crocin")
    prescription = models.CharField(("Prescription"),max_length=500,null=False,default="Y")
    Type_of_Sell = models.CharField(("Type of Sell"),max_length=500,null=True)
    manufacturer = models.CharField(("Manufacturer"),max_length=500,null=False,default="Cipla")
    salt = models.CharField(("Salt"),max_length=500,null=True)
    mrp = models.CharField(("MRP"),max_length=500,null=False,default='50')
    uses = models.CharField(("Uses"),max_length=500,null=True)
    Side_Effects = models.CharField(("Side Effects"),max_length=500,null=True)

    def __str__(self):
        return self.med_name

# class prescription(models.Model):
    # date=models.DateField(auto_now_add=True)
    # med_name=models.CharField(max_length=200)
    # quantity=models.IntegerField()

class Order(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered'),
    )

    date_created = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    medicines = models.ForeignKey(Medicine,null=True,on_delete=models.SET_NULL)
    status = models.CharField(max_length=200,null=True,choices=STATUS)

    def __str__(self):
        return self.medicines

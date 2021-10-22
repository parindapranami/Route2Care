from django.db import models
from django.contrib.auth.models import User
from django.db.models.expressions import F
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

class Medicine(models.Model):
    med_name = models.CharField(("Medicine Name"),max_length=200,null=False,default="Crocin")
    image = models.CharField(("Images"),max_length=1000,null=False,default="https://newassets.apollo247.com/pub/media/catalog/product/a/z/aza0002.jpg")
    prescription = models.CharField(("Prescription"),max_length=500,null=False,default="Y")
    Type_of_Sell = models.CharField(("Type of Sell"),max_length=500,null=True)
    manufacturer = models.CharField(("Manufacturer"),max_length=500,null=False,default="Cipla")
    salt = models.CharField(("Salt"),max_length=500,null=True)
    mrp = models.FloatField(("MRP"),null=False,default=50)
    uses = models.CharField(("Uses"),max_length=500,null=True)
    Side_Effects = models.CharField(("Side Effects"),max_length=500,null=True)

    def __str__(self):
        return self.med_name

class Prescription(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    med = models.CharField(("Medicine Name"),max_length=200,null=False,default="Crocin")
    pres=models.FileField(null=False,upload_to='Prescriptions')


class Order(models.Model):

    date_created = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    medicines = models.ForeignKey(Medicine,null=True,on_delete=models.SET_NULL)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = True
        orderitems = self.orderitem_set.all()
        # for i in orderitems:
        # 	if i.product.digital == False:
        # 		shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total 

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total 

class OrderItem(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.order

    @property
    def get_total(self):
        total = float(self.medicine.mrp) * float(self.quantity)
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage
# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.FloatField()
    description=models.TextField()
    image=models.ImageField(upload_to='products/',storage=MediaCloudinaryStorage())
    categoary=models.CharField(max_length=100,blank=True,null=True)
    stock=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Customer(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Order(models.Model):
    user=models.ForeignKey(Customer,on_delete=models.CASCADE)
    total_price=models.IntegerField()
    payment_method=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f' order #{self.user}'
    
class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    price=models.IntegerField()
    qty=models.IntegerField()

    def __str__(self):
        return self.product.name


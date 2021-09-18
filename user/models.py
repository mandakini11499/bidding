from django.db import models

class RegisterModel(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    contact=models.IntegerField(unique=True)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=40)
    status=models.CharField(max_length=30)
    doj=models.DateField(auto_now_add=True)

class ProductModel(models.Model):
    pno=models.AutoField(primary_key=True)
    pname=models.CharField(max_length=40)
    pinfo=models.TextField()
    image=models.FileField(upload_to='products/')
    bprice=models.FloatField()
    status=models.CharField(max_length=40)
    uid=models.ForeignKey(RegisterModel,on_delete=models.CASCADE)
    
class BidtableModel(models.Model):
    bid=models.AutoField(primary_key=True)
    pno=models.ForeignKey(ProductModel,on_delete=models.CASCADE)
    amount=models.FloatField()
    uid=models.ForeignKey(RegisterModel,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    time=models.TimeField(auto_now_add=True)
from django.db import models

# Create your models here.


class Category(models.Model):
    category_name=models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

class product(models.Model):
    product_name=models.CharField(max_length=100)
    product_price=models.IntegerField()
    product_rating=models.IntegerField()
    product_image=models.ImageField(upload_to='images/')
    product_description=models.TextField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name
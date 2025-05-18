from django.db import models
from category.models import Category
# Create your models here.


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)  
    sku = models.CharField(max_length=50, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    @classmethod
    def create_from_request(cls, data, files):
        return cls.objects.create(
            name=data['pname'],
            description=data['description'],
            price=data['price'],
            stock=data['stock'],
            sku=data['sku'],
            image=files['image'],
            category_id=data['category']
        )    

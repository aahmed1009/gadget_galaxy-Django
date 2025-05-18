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
    status = models.BooleanField(default=True)

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
    @classmethod
    def get_all(cls):
        return cls.objects.filter(status=True)

    @classmethod
    def soft_delete(cls, id):
        product = cls.objects.filter(pk=id).first()
        if product:
            product.status = False
            product.save()
        return product

    @classmethod
    def hard_delete(cls, id):
        return cls.objects.filter(pk=id).delete()
    @classmethod
    def update_product(cls, id, data):
        product = cls.objects.filter(pk=id).first()
        if product:
            product.name = data.get('name', product.name)
            product.description = data.get('description', product.description)
            product.price = data.get('price', product.price)
            product.stock = data.get('stock', product.stock)
            product.sku = data.get('sku', product.sku)
            product.category_id = data.get('category_id', product.category_id)
            if data.get('image'):
                product.image = data.get('image')
            product.save()
        return product

from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.slug}/'
    
    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    thumbnail = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'
  
    def getImage(self):
        if self.image:
            return 'http://localhost:8000' + self.image.url
        return ''
    def getThumbnail(self):
        if self.thumbnail:
            return 'http://localhost:8000' + self.thumbnail.url
        else:
            if self.image:
                return 'http://localhost:8000' + self.image.url
            return ''
        
    def makethumbnail(self):
        if self.image and not self.thumbnail:
            from PIL import Image
            from io import BytesIO
            from django.core.files.base import ContentFile
            
            image = Image.open(self.image)
            image.convert('RGB')
            image.thumbnail((300, 200))
            
            thumb_io = BytesIO()
            image.save(thumb_io, format='JPEG', quality=85)
            
            thumbnail_name = self.image.name.replace('products/', 'products/thumbnails/')
            self.thumbnail.save(thumbnail_name, ContentFile(thumb_io.getvalue()), save=False)
from django.db import models
class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('hot','Hot'),
        ('sweets', 'Sweets'),
        ('Snacks', 'Snacks'),
        ('powders', 'Powders'),
        
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    price = models.FloatField()
    image_path = models.CharField(max_length=200)
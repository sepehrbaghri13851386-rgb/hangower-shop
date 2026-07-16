from django.db import models

class Shop(models.Model):
    CATEGORY_CHOICES = [
        ('general', 'General'),
        ('nike', 'Nike'),
    ]

    title = models.CharField(max_length=30)
    discribshen = models.TextField()
    gheymat = models.DecimalField(max_digits=15, decimal_places=0)
    image = models.ImageField(upload_to='image/Shop')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='general')
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
from django.db import models


class kharid (models.Model):
    title = models.CharField(max_length=30)
    discribshen = models.TextField()
    image = models.ImageField(upload_to='images/kharid')
    gheymat = models.DecimalField(max_digits=15, decimal_places=0)

    def __str__(self):
        return self.title

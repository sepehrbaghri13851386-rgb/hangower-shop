from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Cart(models.Model):
    session_key = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart ({self.session_key})"

    def get_total(self):
        return sum(item.get_subtotal() for item in self.items.all())

    def get_count(self):
        return sum(item.quantity for item in self.items.all())


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    product = GenericForeignKey('content_type', 'object_id')
    quantity = models.PositiveIntegerField(default=1)

    # class Meta:
    #     unique_together = ('cart', 'content_type', 'object_id')

    def __str__(self):
        return f"{self.product.title} x {self.quantity}"

    def get_subtotal(self):
        return self.product.gheymat * self.quantity


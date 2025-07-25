from django.db import models
from django.contrib.auth.models import User
from panther_store.models import Product

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')  # so each user can have only one entry per product

    def __str__(self):
        return f"{self.user.username} - {self.product.name} (x{self.quantity})"

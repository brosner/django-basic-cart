
from django.db import models
from django.contrib.auth.models import User

class Cart(models.Model):
    user = models.ForeignKey(User)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart)


from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

class Cart(models.Model):
    """
    A basic cart.
    """
    user = models.ForeignKey(User, null=True)

class CartItem(models.Model):
    """
    Defines a loose interface between a cart and some other object.
    """
    cart = models.ForeignKey(Cart)
    object_pk = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType)
    product = generic.GenericForeignKey("object_pk", "content_type")

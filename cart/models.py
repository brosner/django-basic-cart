
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

class Cart(models.Model):
    user = models.ForeignKey(User)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart)
    object_pk = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType)
    product = generic.GenericForeignKey("object_pk", "content_type")

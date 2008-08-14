
from django.contrib import admin

from cart.models import Cart, CartItem

class CartItemInline(admin.TabularInline):
    model = CartItem

class CartAdmin(admin.ModelAdmin):
    inlines = [
        CartItem,
    ]

admin.site.register(Cart, CartAdmin)

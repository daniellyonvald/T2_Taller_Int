from django.contrib import admin

# Register your models here.

from.models import Hamburgesa, Ingrediente

admin.site.register(Ingrediente)
admin.site.register(Hamburgesa)
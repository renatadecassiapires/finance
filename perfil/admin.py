from django.contrib import admin
from .models import Conta, Categoria      # trazer as models q criei para a area administrativa do django


# Register your models here.

admin.site.register(Conta)
admin.site.register(Categoria)

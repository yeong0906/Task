from django.contrib import admin
from polls.models import Shoe
from .models import Shoe,Accessories
# Register your models here.

admin.site.register(Shoe)
admin.site.register(Accessories)


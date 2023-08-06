from django.contrib import admin
from .models import Destination, City, Photo

# Register your models here.
admin.site.register(Destination)
admin.site.register(City)
admin.site.register(Photo)


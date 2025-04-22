from django.contrib import admin
from .models import Brand, PhoneModel, Review  # Import your models

admin.site.register(Brand)
admin.site.register(PhoneModel)
admin.site.register(Review)

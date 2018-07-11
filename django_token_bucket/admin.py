from django.contrib import admin

# Register your models here.
from .models import TokenBucket

admin.site.register(TokenBucket)

from django.contrib import admin

# Register your models here.
from .models import Toon, Comment

admin.site.register(Toon)
admin.site.register(Comment)
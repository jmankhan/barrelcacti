from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Album)
admin.site.register(Track)
admin.site.register(Member)
admin.site.register(Story)
admin.site.register(Image)
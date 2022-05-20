from django.contrib import admin

# Register your models here.
from .models import  CryptString, Machine, Message, Blog, Topics

admin.site.register(Topics)
admin.site.register(Blog)
admin.site.register(Message)
admin.site.register(Machine)
admin.site.register(CryptString)
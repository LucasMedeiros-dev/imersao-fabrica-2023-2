from django.contrib import admin
from .models import User
# Register your models here.

# modelo como demonstrado na aula

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     model = User
    
#     fields = ['name','email']

admin.site.register(User) # endpoint finalizado

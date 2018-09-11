from django.contrib import admin
from . import models
 
# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name')

class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name','age')
 
admin.site.register(models.Person,admin.ModelAdmin)
admin.site.register(models.Animal,AnimalAdmin)
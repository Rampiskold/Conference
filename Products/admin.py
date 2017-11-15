from django.contrib import admin
from .models import *


class GenreAdmin(admin.ModelAdmin):
    list_display = ["id","genre"] # на сайте в админке указываем те поля, которые мы хотим видеть
    search_fields = [field.name for field in Genre._meta.fields] # на сайте в админке можем искать в поисковике

    class Meta:
        model = Genre

admin.site.register(Genre, GenreAdmin)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ["id","name"]
    search_fields = [field.name for field in Customers._meta.fields]

    class Meta:
        model = Customers

admin.site.register(Customers, CustomerAdmin)


class DeveloperAdmin(admin.ModelAdmin):
    list_display = ["id","name"]
    search_fields = [field.name for field in Developers._meta.fields] 

    class Meta:
        model = Developers

admin.site.register(Developers, DeveloperAdmin)


class GameAdmin(admin.ModelAdmin):
    list_display = ["id","name","dev"]
    search_fields = [field.name for field in Games._meta.fields]
    
    class Meta:
        model = Games

admin.site.register(Games, GameAdmin)


class ImageAdmin(admin.ModelAdmin):
    list_display = ["id"]
    search_fields = [field.name for field in Images._meta.fields]

    class Meta:
        model = Images

admin.site.register(Images, ImageAdmin)

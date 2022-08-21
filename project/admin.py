from django.contrib import admin
from .models import Project, Category
# Register your models here.
admin.site.register(Category)
admin.site.register(Project)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
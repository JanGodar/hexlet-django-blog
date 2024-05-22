from django.contrib import admin
from django.contrib.admin import DateFieldListFilter
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    search_fields= ['name', 'body']

admin.site.register(Article, ArticleAdmin)

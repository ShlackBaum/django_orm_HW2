from django.contrib import admin

from .models import Article, Scope, ArticleScope

class ArticleScope(admin.TabularInline):
    model = ArticleScope

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_filter = ["id", "title", "published_at", "image"]
    inlines = [ArticleScope,]

@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    list_filter = ['id', 'name']


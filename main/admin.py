from django.contrib import admin
from .models import Category, Product
from review.models import Comment,Rating

class RatingInLine(admin.TabularInlinebular):
    model=Rating

class CommentInLine(admin.TabularInline):
    model = Comment


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category','status']
    list_filter = ['category', 'status']
    search_fields = ['title', 'description']
    inlines = [CommentInLine]
    inlines = [RatingInLine]

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)

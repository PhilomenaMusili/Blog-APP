from django.contrib import admin
from .models import   Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_at', 'status')
    search_fields = ('title', 'author', 'content')
    list_filter = ('status', 'published_at', 'category')

admin.site.register(Post,PostAdmin)

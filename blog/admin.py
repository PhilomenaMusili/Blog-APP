from django.contrib import admin
from .models import   Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_created', 'status')
    search_fields = ('title', 'author', 'content')
    list_filter = ('status', 'date_created', 'category')

admin.site.register(Post,PostAdmin)

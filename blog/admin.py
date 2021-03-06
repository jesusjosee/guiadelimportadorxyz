from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'author', 'publish')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status',)

admin.site.register(Post, PostAdmin)

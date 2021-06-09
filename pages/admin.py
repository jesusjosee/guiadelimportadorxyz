from django.contrib import admin
from . models import Page

# Register your models here.

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ['order']

admin.site.register(Page, PageAdmin)
from django.contrib import admin
from .models import Post, Tag

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    prepopulated_fields = {'slug': ('title',)}

    








admin.site.register(Post, PostAdmin)
admin.site.register(Tag)



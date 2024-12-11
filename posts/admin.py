from django.contrib import admin

# Register your models here.
from posts.models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "publish", "created_on", "last_updated",)
    list_editable = ("publish",)

admin.site.register(BlogPost, BlogPostAdmin)
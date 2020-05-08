from django.contrib import admin

# This allows the models to be viewed and edited in admin.

from .models import Post

admin.site.register(Post)
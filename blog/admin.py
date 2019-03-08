from django.contrib import admin
from .models import Post

admin.site.register(Post)

class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'bio', 'web')

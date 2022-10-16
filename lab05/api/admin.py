from django.contrib import admin
from api.models import Post

admin.site.register(Post)

admin.site.site_header = "My site Admin"
admin.site.site_title = "My site Admin"

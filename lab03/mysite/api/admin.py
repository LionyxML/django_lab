from django.contrib import admin
from api.models import Music

admin.site.register(Music)

admin.site.site_header = "Music API Admin"
admin.site.site_title = "Music API"


# Another way of seeting Admin
#
# class MyAdminSite(AdminSite):
#     # Text to put at the end of each page's <title>.
#     site_title = ugettext_lazy("My site admin")

#     # Text to put in each page's <h1> (and above login form).
#     site_header = ugettext_lazy("My administration")

#     # Text to put at the top of the admin index page.
#     index_title = ugettext_lazy("Site administration")


# admin_site = MyAdminSite()

from django.contrib import admin
from django.urls import path, include
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],

urlpatterns = [
  path("admin/", admin.site.urls),
  path("", include("api.urls")),
]


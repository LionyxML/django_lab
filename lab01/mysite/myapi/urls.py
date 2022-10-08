from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r"Heroes", views.HeroViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "api-auth/", include("rest_framework.urls", namespace="rest_framework")
    ),
]


# We could also be using standard DRF Views (https://www.django-rest-framework.org/api-guide/views/)
# in this case a router is not needed and we could just add the view with:
# path('path/to/my/view/', MySimpleView.as_view())

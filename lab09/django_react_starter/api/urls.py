from django.urls import path, include
from .views import TodoListView
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"todo", TodoListView)


urlpatterns = [
    path("", include(router.urls)),
]

from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post
from rest_framework.permissions import IsAuthenticated


class PostViewSet(viewsets.ModelViewSet):
    """Performs operations with posts"""

    permissions_classes = (IsAuthenticated,)
    queryset = Post.objects.all().order_by("created_at")
    serializer_class = PostSerializer

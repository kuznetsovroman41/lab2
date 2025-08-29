from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from webapp.models import Post, Like
from .serializers import PostSerializer
from .permissions import IsOwnerOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().select_related('author').prefetch_related('likes')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly & IsOwnerOrReadOnly]

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['request'] = self.request
        return ctx

    def perform_create(self, serializer):
        serializer.save()

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def like(self, request, pk=None):
        post = self.get_object()
        Like.objects.get_or_create(user=request.user, post=post)
        return Response({'status': 'liked', 'likes_count': post.likes.count()})

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def unlike(self, request, pk=None):
        post = self.get_object()
        Like.objects.filter(user=request.user, post=post).delete()
        return Response({'status': 'unliked', 'likes_count': post.likes.count()})


from rest_framework import serializers
from webapp.models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    likes_count = serializers.IntegerField(read_only=True)
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'author', 'image', 'description', 'created_at', 'likes_count', 'is_liked']
        read_only_fields = ['id', 'author', 'created_at', 'likes_count', 'is_liked']

    def get_is_liked(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return obj.likes.filter(user=user).exists()
        return False

    def create(self, validated_data):
        request = self.context['request']
        return Post.objects.create(author=request.user, **validated_data)

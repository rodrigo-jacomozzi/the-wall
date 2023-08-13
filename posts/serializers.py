from rest_framework import serializers

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'created', 'text', 'user', ]

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user

        return super(PostSerializer, self).create(validated_data)

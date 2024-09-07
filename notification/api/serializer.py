from rest_framework import serializers

from notification.models import Category, Channel, BackendUser


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'is_active']

class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ['id', 'name', 'description']

class BackendUserSerializer(serializers.ModelSerializer):
    subscribed_categories = CategorySerializer(read_only=True, many=True)
    channels = ChannelSerializer(read_only=True, many=True)
    class Meta:
        model = BackendUser
        fields = ['id', 'name', 'email', 'phone', 'subscribed_categories', 'channels']

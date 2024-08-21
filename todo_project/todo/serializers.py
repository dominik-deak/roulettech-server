from rest_framework import serializers
from .models import TodoItem


class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = "__all__"

    def validate_title(self, value):
        if not value:
            raise serializers.ValidationError("Title cannot be empty.")
        if len(value) > 255:
            raise serializers.ValidationError("Title cannot exceed 255 characters.")
        return value

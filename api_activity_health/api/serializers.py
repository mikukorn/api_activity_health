from rest_framework import serializers
from .models import Activity, DaySummary, Tag, TagActivity


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)


class ActivitySerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = Activity
        fields = ('user', 'type', 'value', 'created_at', 'tags')

    def create(self, validated_data):
        if 'tags' not in self.initial_data:
            activity = Activity.objects.create(**validated_data)
            return activity

        tags = validated_data.pop('tags')
        activity = Activity.objects.create(**validated_data)
        for tag in tags:
            current_tag, status = Tag.objects.get_or_create(**tag)
            TagActivity.objects.create(tag=current_tag, activity=activity)
        return activity


class DaySummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = DaySummary
        fields = ('user', 'type', 'value', 'created_at')

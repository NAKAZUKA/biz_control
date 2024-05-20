from rest_framework import serializers
from .models import WorkSpace


class WorkSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkSpace
        fields = '__all__'

    def create(self, validated_data):
        # Проверка прав доступа на уровне сериализатора
        user = self.context['request'].user
        if user.role not in ['admin', 'owner']:
            raise serializers.ValidationError(
                "You do not have permission to create a workspace."
            )
        work_space = WorkSpace.objects.create(**validated_data)
        return work_space

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

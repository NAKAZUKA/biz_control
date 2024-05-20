from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    work_space_name = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ['id',
                  'username',
                  'password',
                  'email',
                  'first_name',
                  'last_name',
                  'phone_number',
                  'role',
                  'specialty',
                  'position',
                  'workspaces',
                  'work_space_name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

    def get_work_space_name(self, obj):
        if obj.workspaces:
            return obj.workspaces.title
        else:
            return None

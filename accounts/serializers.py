from rest_framework import serializers


class ResendOtpSerializer(serializers.Serializer):
    session_id = serializers.CharField(max_length=100)
    def create(self, validated_data):
        return validated_data
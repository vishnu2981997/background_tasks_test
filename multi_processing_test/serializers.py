from rest_framework import serializers

from .models import ImportRequest


class ImportRequestSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    url = serializers.EmailField(
        required=True,
    )
    access_token = serializers.EmailField(
        required=True,
    )
    queue_url = serializers.EmailField(
        required=True,
    )

    # For displaying error messages

    def __init__(self, *args, **kwargs):
        super(ImportRequestSerializer, self).__init__(*args, **kwargs)

    class Meta:
        model = ImportRequest
        fields = [
            "owner",
            "id",
            "url",
            "access_token",
            "queue_url",
            "running",
            "created",
            "started",
            "ended"
        ]

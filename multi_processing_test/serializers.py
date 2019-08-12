from rest_framework import serializers

from .models import ImportRequest


class ImportRequestSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    url = serializers.CharField(
        required=True,
    )
    access_token = serializers.CharField(
        required=True,
    )
    queue_url = serializers.CharField(
        required=True,
    )

    # For displaying error messages

    def __init__(self, *args, **kwargs):
        super(ImportRequestSerializer, self).__init__(*args, **kwargs)

    class Meta:
        model = ImportRequest
        # add "owner" to fields to display ownership
        fields = [
            "id",
            "url",
            "access_token",
            "queue_url",
            "running",
            "created",
            "started",
            "ended"
        ]

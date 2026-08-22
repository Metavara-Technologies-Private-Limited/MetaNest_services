from rest_framework import serializers


class WaiveLateFeeSerializer(serializers.Serializer):

    history_id = serializers.UUIDField()

    waived_amount = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        min_value=0
    )

    waiver_reason = serializers.CharField(
        required=True,
        allow_blank=False
    )
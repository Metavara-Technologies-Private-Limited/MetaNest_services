from rest_framework import serializers


class CollectionSummarySerializer(serializers.Serializer):
    total_billed = serializers.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    total_collected = serializers.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    total_outstanding = serializers.DecimalField(
        max_digits=12,
        decimal_places=2,
    )


class CollectionTrendSerializer(serializers.Serializer):
    month = serializers.CharField()

    collected = serializers.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    outstanding = serializers.DecimalField(
        max_digits=12,
        decimal_places=2,
    )


class CollectionReportSerializer(serializers.Serializer):
    total_billed = serializers.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    total_collected = serializers.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    total_outstanding = serializers.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    collection_trend = CollectionTrendSerializer(
        many=True,
    )


class OutstandingReportSerializer(serializers.Serializer):
    total_billed = serializers.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    total_collected = serializers.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    total_outstanding = serializers.DecimalField(
        max_digits=12,
        decimal_places=2,
    )


class OccupancyReportSerializer(serializers.Serializer):
    total_flats = serializers.IntegerField()

    occupied_flats = serializers.IntegerField()

    vacant_flats = serializers.IntegerField()

    occupancy_percentage = serializers.DecimalField(
        max_digits=6,
        decimal_places=2,
    )

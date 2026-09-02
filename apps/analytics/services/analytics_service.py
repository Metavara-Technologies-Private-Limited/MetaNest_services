from decimal import Decimal

from django.db.models import Sum
from django.db.models.functions import TruncMonth

from apps.apartment_master.models import Flat
from apps.finance.models.Bill import Bill
from apps.finance.models.Payment import Payment
from apps.people.models import Resident


ZERO = Decimal("0.00")


def get_collection_report():
    """
    Collection analytics.

    Returns:
        - total billed
        - total collected
        - total outstanding
        - monthly collection trend
    """

    bills = Bill.objects.filter(is_deleted=False)

    successful_payments = Payment.objects.filter(
        is_deleted=False,
        payment_status=Payment.PAYMENT_STATUS_SUCCESS,
    )

    total_billed = (
        bills.aggregate(total=Sum("total_amount"))["total"]
        or ZERO
    )

    total_collected = (
        successful_payments.aggregate(total=Sum("amount"))["total"]
        or ZERO
    )

    total_outstanding = max(
        total_billed - total_collected,
        ZERO,
    )

    monthly_bills = (
        bills
        .annotate(month=TruncMonth("billing_month"))
        .values("month")
        .annotate(billed=Sum("total_amount"))
        .order_by("month")
    )

    collection_trend = []

    for item in monthly_bills:
        month = item["month"]

        collected = (
            successful_payments
            .filter(
                payment_date__year=month.year,
                payment_date__month=month.month,
            )
            .aggregate(total=Sum("amount"))["total"]
            or ZERO
        )

        billed = item["billed"] or ZERO

        outstanding = max(
            billed - collected,
            ZERO,
        )

        collection_trend.append(
            {
                "month": month.strftime("%b"),
                "collected": collected,
                "outstanding": outstanding,
            }
        )

    return {
        "total_billed": total_billed,
        "total_collected": total_collected,
        "total_outstanding": total_outstanding,
        "collection_trend": collection_trend,
    }


def get_outstanding_report():
    """
    Outstanding analytics.

    Calculates the current total billed,
    collected and outstanding amounts.
    """

    bills = Bill.objects.filter(is_deleted=False)

    successful_payments = Payment.objects.filter(
        is_deleted=False,
        payment_status=Payment.PAYMENT_STATUS_SUCCESS,
    )

    total_billed = (
        bills.aggregate(total=Sum("total_amount"))["total"]
        or ZERO
    )

    total_collected = (
        successful_payments.aggregate(total=Sum("amount"))["total"]
        or ZERO
    )

    total_outstanding = max(
        total_billed - total_collected,
        ZERO,
    )

    return {
        "total_billed": total_billed,
        "total_collected": total_collected,
        "total_outstanding": total_outstanding,
    }


def get_occupancy_report():
    """
    Occupancy analytics.

    A flat is considered occupied when it has
    at least one active resident.
    """

    flats = Flat.objects.filter(
        is_deleted=False,
        is_active=True,
    )

    active_residents = Resident.objects.filter(
        status="Active",
    )

    total_flats = flats.count()

    occupied_flats = (
        flats
        .filter(residents__in=active_residents)
        .distinct()
        .count()
    )

    vacant_flats = max(
        total_flats - occupied_flats,
        0,
    )

    if total_flats:
        occupancy_percentage = (
            Decimal(occupied_flats)
            / Decimal(total_flats)
            * Decimal("100")
        ).quantize(Decimal("0.01"))
    else:
        occupancy_percentage = ZERO

    return {
        "total_flats": total_flats,
        "occupied_flats": occupied_flats,
        "vacant_flats": vacant_flats,
        "occupancy_percentage": occupancy_percentage,
    }

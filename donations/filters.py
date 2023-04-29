import django_filters
from django.forms import TextInput, NumberInput
from django_filters.widgets import RangeWidget

from donations.models import Donation


class DonationFilter(django_filters.FilterSet):
    nickname = django_filters.CharFilter(
        field_name="nickname",
        lookup_expr="icontains",
        label="Нікнейм",
        widget=TextInput(attrs={"placeholder": "Нікнейм"}),
    )
    amount_gt = django_filters.NumberFilter(
        field_name="amount",
        lookup_expr="gte",
        label="Сума більше ніж (включно)",
        widget=NumberInput(attrs={"placeholder": "Сума"}),
    )
    amount_lt = django_filters.NumberFilter(
        field_name="amount",
        lookup_expr="lte",
        label="Сума менше ніж (включно)",
        widget=NumberInput(attrs={"placeholder": "Сума"}),
    )
    created_at = django_filters.DateFromToRangeFilter(
        field_name="created_at",
        label="Дата",
        widget=RangeWidget(attrs={"type": "date"}),
    )

    class Meta:
        model = Donation
        fields = ["nickname", "amount_gt", "amount_lt", "created_at"]

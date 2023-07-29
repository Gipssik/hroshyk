import django_filters
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, HTML
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(Column("nickname", "amount_gt", "amount_lt"), Column("created_at")),
            HTML(
                """
                <div class="buttons">
                    <button type="submit" class="twitch-btn">
                        Пошук
                    </button>
                    <a href="{% url 'donations' %}" class="simple-btn">Скинути</a>
                </div>
            """
            ),
        )

    @property
    def form(self):
        self.helper.disable_csrf = self.request.method == "GET"
        if hasattr(self, "_form") and not hasattr(self._form, "helper"):
            self._form.helper = self.helper
        form = super().form
        if not hasattr(form, "helper"):
            form.helper = self.helper
        return form

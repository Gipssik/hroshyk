import django_filters
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, HTML
from django.forms import TextInput, NumberInput
from django_filters.widgets import RangeWidget
from django.utils.translation import gettext_lazy as _

from donations.models import Donation


class DonationFilter(django_filters.FilterSet):
    nickname = django_filters.CharFilter(
        field_name="nickname",
        lookup_expr="icontains",
        label=_("Nickname"),
        widget=TextInput(attrs={"placeholder": _("Nickname")}),
    )
    amount_gt = django_filters.NumberFilter(
        field_name="amount",
        lookup_expr="gte",
        label=_("Amount more than (inclusive)"),
        widget=NumberInput(attrs={"placeholder": _("Amount")}),
    )
    amount_lt = django_filters.NumberFilter(
        field_name="amount",
        lookup_expr="lte",
        label=_("Amount less than (inclusive)"),
        widget=NumberInput(attrs={"placeholder": _("Amount")}),
    )
    created_at = django_filters.DateFromToRangeFilter(
        field_name="created_at",
        label=_("Date"),
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
                {% load i18n %}
                
                <div class="buttons">
                    <button type="submit" class="twitch-btn">
                        {% trans "Search" %}
                    </button>
                    <a href="{% url 'donations' %}" class="simple-btn">{% trans "Reset" %}</a>
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

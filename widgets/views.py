from django.views.generic import ListView, UpdateView

from accounts.auth import AuthenticationMixin
from widgets.models import DonationWidget, DonationWidgetConfig


class DonationWidgetListView(AuthenticationMixin, ListView):
    template_name = "widgets/donation_widget/donation_widget_list.html"
    model = DonationWidget
    context_object_name = "donation_widgets"
    paginate_by = 50
    ordering = ["id"]


class DonationWidgetUpdateView(AuthenticationMixin, UpdateView):
    template_name = "widgets/donation_widget/donation_widget_update.html"
    model = DonationWidget
    fields = "__all__"


class DonationWidgetConfigUpdateView(AuthenticationMixin, UpdateView):
    template_name = "widgets/donation_widget/donation_widget_config_update.html"
    model = DonationWidgetConfig
    fields = "__all__"

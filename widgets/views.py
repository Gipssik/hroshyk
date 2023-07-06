from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView, RedirectView

from widgets.forms import DonationWidgetForm
from widgets.models import DonationWidget, DonationWidgetConfig


class DonationWidgetListView(LoginRequiredMixin, ListView):
    template_name = "widgets/donation_widget/donation_widget_list.html"
    model = DonationWidget
    context_object_name = "donation_widgets"
    paginate_by = 50
    ordering = ["id"]


class DonationWidgetUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "widgets/donation_widget/donation_widget_update.html"
    model = DonationWidget
    form_class = DonationWidgetForm


class DonationWidgetConfigUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "widgets/donation_widget/donation_widget_config_update.html"
    model = DonationWidgetConfig
    fields = "__all__"


class DonationWidgetLinkView(RedirectView):
    pattern_name = "donation_widgets_update"

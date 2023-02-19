from django.contrib import messages
from django.views.generic import UpdateView

from donation_page.models import DonationPage


class DonationPageView(UpdateView):
    model = DonationPage
    template_name = "donation_page/donation_page.html"
    fields = [
        "page_link",
        "page_title",
        "page_meta",
        "test_mode",
        "title",
        "title_subtext",
        "nickname_placeholder",
        "nickname_min_length",
        "nickname_max_length",
        "amount_placeholder",
        "amount_min",
        "amount_max",
        "message_placeholder",
        "message_min_length",
        "message_max_length",
        "viewer_pays_commision",
        "donate_button_text",
        "target_title",
        "target_amount",
    ]

    def get_object(self, queryset=None):
        return self.request.user.donation_page

    def post(self, request, *args, **kwargs):
        result = super().post(request, *args, **kwargs)
        messages.success(request, "Дані успішно оновлено")
        return result

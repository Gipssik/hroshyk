from django.contrib import messages
from django.forms import Field, CharField, IntegerField
from django.views.generic import UpdateView

from donation_page.models import DonationPage
from donations.forms import DonationForm


def get_donation_form() -> DonationForm:
    form = DonationForm()


class DonationPageView(UpdateView):
    model = DonationPage
    template_name = "donation_page/donation_page.html"
    extra_context = {"donation_form": DonationForm()}
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

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        form: DonationForm = data["donation_form"]
        obj: DonationPage = data["object"]
        for field_name in ("nickname", "amount", "message"):
            field: Field = form.fields[field_name]
            field.widget.attrs["placeholder"] = getattr(obj, f"{field_name}_placeholder")
            if isinstance(field, CharField):
                field.widget.attrs["maxlength"] = getattr(obj, f"{field_name}_max_length")
                field.widget.attrs["minlength"] = getattr(obj, f"{field_name}_min_length")
            elif isinstance(field, IntegerField):
                field.widget.attrs["max"] = getattr(obj, f"{field_name}_max")
                field.widget.attrs["min"] = getattr(obj, f"{field_name}_min")
        return data

    def get_object(self, queryset=None):
        return self.request.user.donation_page

    def post(self, request, *args, **kwargs):
        result = super().post(request, *args, **kwargs)
        messages.success(request, "Дані успішно оновлено")
        return result

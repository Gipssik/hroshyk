from django import forms
from django.forms import ModelForm

from donation_page.models import DonationPage


class LinkInput(forms.TextInput):
    template_name = "forms/copy_link_field.html"


class DonationPageForm(ModelForm):
    class Meta:
        model = DonationPage
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
            "reset_current_target",
        ]

    page_link = forms.CharField(
        widget=LinkInput(attrs={"class": "form-control"}),
        label="Посилання на сторінку",
        required=True,
        disabled=True,
    )
    reset_current_target = forms.BooleanField(initial=False, required=False, label="Скинути зібрану суму")

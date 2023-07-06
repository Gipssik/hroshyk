from django import forms
from django.forms import ModelForm

from donation_page.forms import LinkInput
from widgets.models import DonationWidget


class DonationWidgetForm(ModelForm):
    class Meta:
        model = DonationWidget
        exclude = ["user"]

    link_identifier = forms.CharField(
        widget=LinkInput(
            attrs={
                "class": "form-control",
                "secret": True,
                "url_for": "donation_widgets_link",
                "url_kwarg": "link_identifier",
            }
        ),
        label="Посилання на віджет",
        required=True,
        disabled=True,
    )

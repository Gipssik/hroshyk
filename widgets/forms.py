from crispy_forms.helper import FormHelper
from django import forms
from django.forms import ModelForm, inlineformset_factory
from django.utils.translation import gettext_lazy as _

from donation_page.forms import LinkInput
from widgets.models import DonationWidget, DonationWidgetConfig

donation_widget_config_fields = [
    "image",
    "sound",
    "title_format",
    "min_amount",
    "max_amount",
    "title_font_size",
    "title_color",
    "title_shadow_color",
    "message_font_size",
    "message_color",
    "message_shadow_color",
    "sound_volume",
    "speaker_volume",
]
donation_widget_config_widgets = {
    "title_color": forms.TextInput(attrs={"type": "color"}),
    "title_shadow_color": forms.TextInput(attrs={"type": "color"}),
    "message_color": forms.TextInput(attrs={"type": "color"}),
    "message_shadow_color": forms.TextInput(attrs={"type": "color"}),
    "sound_volume": forms.NumberInput(attrs={"type": "range", "min": 0, "max": 100}),
    "speaker_volume": forms.NumberInput(attrs={"type": "range", "min": 0, "max": 100}),
}


class CreateDonationWidgetForm(ModelForm):
    class Meta:
        model = DonationWidget
        fields = ["name"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

    name = forms.CharField(
        max_length=255,
        label=_("Widget name"),
        widget=forms.TextInput(attrs={"placeholder": _("Widget name")}),
    )


DonationWidgetConfigFormSet = inlineformset_factory(
    DonationWidget,
    DonationWidgetConfig,
    fields=donation_widget_config_fields,
    widgets=donation_widget_config_widgets,
    extra=1,
    can_delete=False,
)


class DonationWidgetForm(ModelForm):
    class Meta:
        model = DonationWidget
        exclude = ["user"]

    link_identifier = forms.CharField(
        widget=LinkInput(
            attrs={
                "class": "form-control",
                "secret": True,
                "url_for": "donation_alert",
                "url_kwarg": "widget_identifier",
            }
        ),
        label=_("Widget link"),
        required=True,
        disabled=True,
    )


class DonationWidgetConfigForm(ModelForm):
    class Meta:
        model = DonationWidgetConfig
        fields = donation_widget_config_fields
        widgets = donation_widget_config_widgets

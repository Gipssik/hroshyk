from crispy_forms.helper import FormHelper
from django import forms
from django.core import validators
from django.forms import ModelForm, inlineformset_factory

from donation_page.forms import LinkInput
from widgets.models import DonationWidget, DonationWidgetConfig


class CreateDonationWidgetForm(ModelForm):
    class Meta:
        model = DonationWidget
        fields = ["name"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

    name = forms.CharField(
        max_length=255,
        label="Назва віджета",
        widget=forms.TextInput(attrs={"placeholder": "Назва віджета"}),
    )


DonationWidgetConfigFormSet = inlineformset_factory(
    DonationWidget,
    DonationWidgetConfig,
    fields=[
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
    ],
    widgets={
        "title_color": forms.TextInput(attrs={"type": "color"}),
        "title_shadow_color": forms.TextInput(attrs={"type": "color"}),
        "message_color": forms.TextInput(attrs={"type": "color"}),
        "message_shadow_color": forms.TextInput(attrs={"type": "color"}),
    },
    extra=1,
    can_delete=False,
)


class DonationWidgetWithConfigForm(forms.Form):
    widget_name = forms.CharField(max_length=255, label="Назва віджета")
    title_format = forms.CharField(initial="{nickname} - {amount}", label="Формат заголовку")
    min_amount = forms.IntegerField(initial=20, label="Мінімальна сума для відображення")
    max_amount = forms.IntegerField(initial=10000, label="Максимальна сума для відображення")
    title_font_size = forms.IntegerField(initial=24, label="Розмір шрифту заголовку")
    title_color = forms.CharField(
        widget=forms.TextInput(attrs={"type": "color"}),
        initial="#ffffff",
        label="Колір заголовку",
    )
    title_shadow_color = forms.CharField(
        widget=forms.TextInput(attrs={"type": "color"}),
        initial="#000000",
        label="Колір тіні заголовку",
    )
    message_font_size = forms.IntegerField(initial=20, label="Розмір шрифту повідомлення")
    message_color = forms.CharField(
        widget=forms.TextInput(attrs={"type": "color"}),
        initial="#ffffff",
        label="Колір повідомлення",
    )
    message_shadow_color = forms.CharField(
        widget=forms.TextInput(attrs={"type": "color"}),
        initial="#000000",
        label="Колір тіні повідомлення",
    )
    image = forms.ImageField(label="Зображення")
    sound = forms.FileField(
        validators=[validators.FileExtensionValidator(allowed_extensions=["mp3", "wav", "ogg", "m4a", "flac"])],
    )
    sound_volume = forms.IntegerField(
        widget=forms.NumberInput(attrs={"type": "range", "min": 0, "max": 100}),
        initial=100,
    )
    speaker_volume = forms.IntegerField(initial=100)


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

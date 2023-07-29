from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, HTML, Column
from django import forms

from donations.models import Donation


class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ["nickname", "amount", "message"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(Column("nickname"), Column("amount")),
            Row("message"),
            HTML(
                """
                <div class="submit-btn">
                    {% if is_preview == True %}
                        <div class="twitch-btn">
                            {{ donation_page.donate_button_text }}
                        </div>
                    {% else %}
                        <button type="submit" class="twitch-btn">
                            {{ donation_page.donate_button_text }}
                        </button>
                    {% endif %}
                </div>
            """
            ),
        )


class FullDonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ["nickname", "amount", "message", "streamer"]

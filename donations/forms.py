from django.forms import ModelForm

from donations.models import Donation


class DonationForm(ModelForm):
    class Meta:
        model = Donation
        fields = ["nickname", "amount", "message"]

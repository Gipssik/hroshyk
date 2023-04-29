from django import forms

from donations.models import Donation


class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ["nickname", "amount", "message"]


class FullDonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ["nickname", "amount", "message", "streamer"]

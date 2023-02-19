from django.urls import path

from donation_page.views import DonationPageView

urlpatterns = [
    path("", DonationPageView.as_view(), name="donation_page"),
]

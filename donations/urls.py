from django.urls import path

from donations.views import DonationsView, ViewerDonationPageView

urlpatterns = [
    path("cabinet/donations/", DonationsView.as_view(), name="donations"),
    path("<str:link>/", ViewerDonationPageView.as_view(), name="viewer_donation_page"),
]

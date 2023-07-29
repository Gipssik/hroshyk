from django.urls import path

from donations.views import DonationsListView, ViewerDonationPageView, DonationDetailView

urlpatterns = [
    path("my-cabinet/donations/", DonationsListView.as_view(), name="donations"),
    path("my-cabinet/donations/<int:pk>/", DonationDetailView.as_view(), name="donation_detail"),
    path("<str:link>/", ViewerDonationPageView.as_view(), name="viewer_donation_page"),
]

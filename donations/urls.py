from django.urls import path

from donations.views import DonationsView

urlpatterns = [
    path("", DonationsView.as_view(), name="donations"),
]

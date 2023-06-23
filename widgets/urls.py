from django.urls import path

from widgets.views import DonationWidgetListView, DonationWidgetConfigUpdateView, DonationWidgetUpdateView

urlpatterns = [
    path("donation-widgets/", DonationWidgetListView.as_view(), name="donation_widgets_list"),
    path(
        "donation-widgets/<int:pk>/",
        DonationWidgetUpdateView.as_view(),
        name="donation_widgets_update",
    ),
    path(
        "donation-widgets/config/<int:pk>/",
        DonationWidgetConfigUpdateView.as_view(),
        name="donation_widgets_config_update",
    ),
]

from django.urls import path

from widgets.views import (
    DonationWidgetListView,
    DonationWidgetConfigUpdateView,
    DonationWidgetUpdateView,
    DonationWidgetCreateView,
    DonationWidgetDeleteView,
    DonationWidgetConfigCreateView,
    DonationWidgetConfigDeleteView,
)

urlpatterns = [
    path("donation-widgets/", DonationWidgetListView.as_view(), name="donation_widgets_list"),
    path("donation-widgets/create/", DonationWidgetCreateView.as_view(), name="donation_widgets_create"),
    path("donation-widgets/delete/<int:pk>/", DonationWidgetDeleteView.as_view(), name="donation_widgets_delete"),
    path(
        "donation-widgets/<int:pk>/",
        DonationWidgetUpdateView.as_view(),
        name="donation_widgets_update",
    ),
    path(
        "donation-widgets/config/new/",
        DonationWidgetConfigCreateView.as_view(),
        name="donation_widgets_config_create",
    ),
    path(
        "donation-widgets/config/<int:pk>/",
        DonationWidgetConfigUpdateView.as_view(),
        name="donation_widgets_config_update",
    ),
    path(
        "donation-widgets/config/delete/<int:pk>/",
        DonationWidgetConfigDeleteView.as_view(),
        name="donation_widgets_config_delete",
    ),
]

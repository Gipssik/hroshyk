from django.contrib import admin
from django.urls import path, include

from accounts.views import HomeView
from widgets.views import DonationWidgetLinkView

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "user-widgets/<str:link_identifier>/",
        DonationWidgetLinkView.as_view(),
        name="donation_widgets_link",
    ),
    path("", HomeView.as_view(), name="home"),
    path("", include("donations.urls")),
    path("twitch-auth/", include("django_twitch_auth.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
    path("user-accounts/", include("accounts.urls")),
    path("", include("donations.urls")),
    path("my-cabinet/", include("donation_page.urls")),
    path("my-cabinet/", include("widgets.urls")),
]

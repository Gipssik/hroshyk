from django.contrib import admin
from django.urls import path, include

from accounts.views import HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("", include("django_twitch_auth.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
    path("accounts/", include("accounts.urls")),
    path("donations/", include("donations.urls")),
    path("donation-page/", include("donation_page.urls")),
    path("admin/", admin.site.urls),
]

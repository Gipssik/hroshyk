from django.contrib import admin
from django.urls import path, include

from accounts.views import HomeView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomeView.as_view(), name="home"),
    path("", include("django_twitch_auth.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
    path("accounts/", include("accounts.urls")),
    path("", include("donations.urls")),
    path("cabinet/", include("donation_page.urls")),
]

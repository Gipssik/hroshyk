from django.contrib import admin
from django.urls import path, include
from django.utils import timezone
from django.views.decorators.http import last_modified
from django.views.i18n import JavaScriptCatalog

from accounts.views import HomeView
from widgets.views import DonationAlertView

last_modified_date = timezone.now()

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "jsi18n/",
        last_modified(lambda req, **kw: last_modified_date)(JavaScriptCatalog.as_view()),
        name="javascript-catalog",
    ),
    path("user-widgets/<str:widget_identifier>/", DonationAlertView.as_view(), name="donation_alert"),
    path("", HomeView.as_view(), name="home"),
    path("", include("donations.urls")),
    path("twitch-auth/", include("django_twitch_auth.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
    path("user-accounts/", include("accounts.urls")),
    path("", include("donations.urls")),
    path("my-cabinet/", include("donation_page.urls")),
    path("my-cabinet/", include("widgets.urls")),
]

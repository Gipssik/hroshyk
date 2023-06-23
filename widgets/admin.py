from django.contrib import admin

from widgets.models import DonationWidget, DonationWidgetConfig

admin.site.register(DonationWidget)
admin.site.register(DonationWidgetConfig)

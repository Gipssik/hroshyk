from django.views.generic import TemplateView


class DonationsView(TemplateView):
    template_name = "donations.html"

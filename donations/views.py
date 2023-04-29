from django.http import Http404, QueryDict
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, CreateView

from accounts.models import Streamer
from donation_page.models import DonationPage
from donations.forms import DonationForm, FullDonationForm
from donations.models import Donation
from donations.utils import donation_add_validation


class DonationsView(TemplateView):
    template_name = "donations.html"


class ViewerDonationPageView(CreateView):
    template_name = "donation_page/viewer_donation_page.html"
    form_class = DonationForm
    object: Donation | None

    def __init__(self):
        super().__init__()

    def get(self, request, *args, **kwargs):
        link = kwargs["link"]
        response = super().get(request, *args, **kwargs)
        response.context_data["donation_page"] = get_object_or_404(DonationPage, page_link=link)
        form = response.context_data["form"]
        obj = response.context_data["donation_page"]
        donation_add_validation(form, obj)
        return response

    def post(self, request, *args, **kwargs):
        self.object = None
        form = FullDonationForm(**self.get_form_kwargs())
        result = self.form_valid(form) if form.is_valid() else self.form_invalid(form)
        if result.status_code < 400:
            self.object.streamer.donation_page.target_current_amount += self.object.amount
            self.object.streamer.donation_page.save()
        return result

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.method != "POST":
            return kwargs
        link = self.kwargs["link"]
        streamer = Streamer.objects.get(donation_page__page_link=link)
        if not streamer:
            raise Http404("Сторінка не знайдена")
        kwargs["data"] = QueryDict(self.request.POST.copy().urlencode(), mutable=True)
        kwargs["data"]["streamer"] = str(streamer.id)
        return kwargs

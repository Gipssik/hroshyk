from django.contrib import messages
from django.http import Http404
from django.views.generic import UpdateView

from accounts.auth import AuthenticationMixin
from donation_page.forms import DonationPageForm
from donation_page.models import DonationPage
from donations.forms import DonationForm
from donations.utils import donation_add_validation


class DonationPageView(AuthenticationMixin, UpdateView):
    model = DonationPage
    template_name = "donation_page/donation_page.html"
    extra_context = {"donation_form": DonationForm()}
    form_class = DonationPageForm

    def get_form(self, form_class=None):
        form: DonationForm = super().get_form(form_class)
        form.fields["page_link"].widget.host = f"{self.request.scheme}://{self.request.get_host()}/"
        return form

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        form: DonationForm = data["donation_form"]
        try:
            obj: DonationPage = data["object"]
        except KeyError:
            return data
        donation_add_validation(form, obj)
        data["is_preview"] = True
        return data

    def get_object(self, queryset=None):
        if not self.request.user.donation_page:
            raise Http404("Сторінка не знайдена")
        return self.request.user.donation_page

    def post(self, request, *args, **kwargs):
        result = super().post(request, *args, **kwargs)
        reset_current_target = request.POST.get("reset_current_target") == "on"
        if reset_current_target:
            self.object.reset_current_target()
        messages.success(request, "Дані успішно оновлено")
        return result

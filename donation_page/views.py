from django.contrib import messages
from django.forms import Field, CharField, IntegerField
from django.http import Http404
from django.views.generic import UpdateView

from donation_page.forms import DonationPageForm
from donation_page.models import DonationPage
from donations.forms import DonationForm


class DonationPageView(UpdateView):
    model = DonationPage
    template_name = "donation_page/donation_page.html"
    extra_context = {"donation_form": DonationForm()}
    form_class = DonationPageForm

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        form: DonationForm = data["donation_form"]
        try:
            obj: DonationPage = data["object"]
        except KeyError:
            return data
        for field_name in ("nickname", "amount", "message"):
            field: Field = form.fields[field_name]
            field.widget.attrs["placeholder"] = getattr(obj, f"{field_name}_placeholder")
            if isinstance(field, CharField):
                field.widget.attrs["maxlength"] = getattr(obj, f"{field_name}_max_length")
                field.widget.attrs["minlength"] = getattr(obj, f"{field_name}_min_length")
            elif isinstance(field, IntegerField):
                field.widget.attrs["max"] = getattr(obj, f"{field_name}_max")
                field.widget.attrs["min"] = getattr(obj, f"{field_name}_min")
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

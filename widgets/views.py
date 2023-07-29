from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import ListView, UpdateView, RedirectView, FormView

from widgets.forms import DonationWidgetForm, CreateDonationWidgetForm, DonationWidgetConfigFormSet
from widgets.models import DonationWidget, DonationWidgetConfig


class DonationWidgetListView(LoginRequiredMixin, ListView):
    template_name = "widgets/donation_widget/donation_widget_list.html"
    model = DonationWidget
    context_object_name = "donation_widgets"
    paginate_by = 50
    ordering = ["id"]

    def get(self, request, *args, **kwargs):
        if request.htmx:
            self.template_name = "widgets/donation_widget/donation_widget_list_content.html"
        else:
            self.template_name = "widgets/donation_widget/donation_widget_list.html"
        return super().get(request, *args, **kwargs)


class DonationWidgetCreateView(LoginRequiredMixin, FormView):
    template_name = "widgets/donation_widget/donation_widget_create.html"
    form_class = CreateDonationWidgetForm
    success_url = "donation_widgets_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context["formset"] = DonationWidgetConfigFormSet(
                self.request.POST,
                self.request.FILES,
                instance=DonationWidget(),
            )
        else:
            context["formset"] = DonationWidgetConfigFormSet(instance=DonationWidget())
        return context

    def form_valid(self, form):
        formset = DonationWidgetConfigFormSet(self.request.POST, self.request.FILES, instance=DonationWidget())
        if formset.is_valid():
            form.instance.user = self.request.user
            donation_widget = form.save()
            instances = formset.save(commit=False)
            for instance in instances:
                instance.donation_widget = donation_widget
                instance.save()

            return redirect(self.get_success_url())

        return self.render_to_response(self.get_context_data(form=form, formset=formset))


class DonationWidgetUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "widgets/donation_widget/donation_widget_update.html"
    model = DonationWidget
    form_class = DonationWidgetForm


class DonationWidgetConfigUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "widgets/donation_widget/donation_widget_config_update.html"
    model = DonationWidgetConfig
    fields = "__all__"


class DonationWidgetLinkView(RedirectView):
    pattern_name = "donation_widgets_update"

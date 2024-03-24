from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Prefetch
from django.http import HttpResponseForbidden, Http404
from django.urls import reverse_lazy
from django.utils.translation import gettext
from django.views.generic import ListView, UpdateView, RedirectView, FormView, DeleteView
from django_htmx.http import HttpResponseLocation

from widgets.forms import (
    DonationWidgetForm,
    CreateDonationWidgetForm,
    DonationWidgetConfigFormSet,
    DonationWidgetConfigForm,
)
from widgets.models import DonationWidget, DonationWidgetConfig


class DonationWidgetListView(LoginRequiredMixin, ListView):
    template_name = "widgets/donation_widget/donation_widget_list.html"
    model = DonationWidget
    context_object_name = "donation_widgets"
    ordering = ["id"]

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user).order_by("id")

    def get(self, request, *args, **kwargs):
        if request.htmx:
            self.template_name = "widgets/donation_widget/donation_widget_list_content.html"
        else:
            self.template_name = "widgets/donation_widget/donation_widget_list.html"
        return super().get(request, *args, **kwargs)


class DonationWidgetCreateView(LoginRequiredMixin, FormView):
    template_name = "widgets/donation_widget/donation_widget_create.html"
    form_class = CreateDonationWidgetForm
    success_url = reverse_lazy("donation_widgets_list")

    def get(self, request, *args, **kwargs):
        if request.htmx:
            self.template_name = "widgets/donation_widget/donation_widget_create_content.html"
        else:
            self.template_name = "widgets/donation_widget/donation_widget_create.html"
        if request.user.donation_widgets.count() >= 3:
            messages.error(request, gettext("You cannot create more than 3 widgets"))
            return HttpResponseForbidden()
        return super().get(request, *args, **kwargs)

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

            return HttpResponseLocation(self.get_success_url(), target="main")

        return self.render_to_response(self.get_context_data(form=form, formset=formset))


class DonationWidgetUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "widgets/donation_widget/donation_widget_update.html"
    model = DonationWidget
    context_object_name = "donation_widget"
    form_class = DonationWidgetForm

    def get(self, request, *args, **kwargs):
        if request.htmx:
            self.template_name = "widgets/donation_widget/donation_widget_update_content.html"
        else:
            self.template_name = "widgets/donation_widget/donation_widget_update.html"
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return self.model.objects.prefetch_related(
            Prefetch("configs", queryset=DonationWidgetConfig.objects.order_by("-id")),
        )

    def form_valid(self, form):
        if self.object.user != self.request.user:
            return HttpResponseForbidden()
        self.object = form.save()
        messages.success(self.request, gettext("Data updated successfully"))

        if self.request.htmx:
            self.template_name = "widgets/donation_widget/donation_widget_update_content.html"
        else:
            self.template_name = "widgets/donation_widget/donation_widget_update.html"

        return self.render_to_response(self.get_context_data(form=form, donation_widget=self.object))


class DonationWidgetDeleteView(LoginRequiredMixin, DeleteView):
    model = DonationWidget
    success_url = reverse_lazy("donation_widgets_list")

    def form_valid(self, form):
        if self.object.user != self.request.user:
            return HttpResponseForbidden()
        self.object.delete()
        return HttpResponseLocation(self.success_url, target="main")


class DonationWidgetConfigCreateView(LoginRequiredMixin, FormView):
    form_class = DonationWidgetConfigForm
    template_name = "widgets/donation_widget/donation_widget_config_create.html"

    def get(self, request, *args, **kwargs):
        if request.htmx:
            self.template_name = "widgets/donation_widget/donation_widget_config_create_content.html"
        else:
            self.template_name = "widgets/donation_widget/donation_widget_config_create.html"
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        donation_widget_id = kwargs.get("donation_widget_id") or int(self.request.GET.get("donation_widget_id"))
        if not donation_widget_id or not DonationWidget.objects.filter(pk=donation_widget_id).exists():
            return Http404()
        context["donation_widget_id"] = donation_widget_id
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        donation_widget_id = int(self.request.GET.get("donation_widget_id"))
        if not donation_widget_id or not DonationWidget.objects.filter(pk=donation_widget_id).exists():
            return Http404()
        self.object.donation_widget_id = donation_widget_id
        self.object.save()
        success_url = reverse_lazy("donation_widgets_config_update", kwargs={"pk": self.object.pk})
        return HttpResponseLocation(success_url, target="main")


class DonationWidgetConfigUpdateView(LoginRequiredMixin, UpdateView):
    model = DonationWidgetConfig
    form_class = DonationWidgetConfigForm
    context_object_name = "donation_widget_config"
    template_name = "widgets/donation_widget/donation_widget_config_update.html"

    def get(self, request, *args, **kwargs):
        if request.htmx:
            self.template_name = "widgets/donation_widget/donation_widget_config_update_content.html"
        else:
            self.template_name = "widgets/donation_widget/donation_widget_config_update.html"
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        if self.object.donation_widget.user != self.request.user:
            return HttpResponseForbidden()
        self.object = form.save()
        messages.success(self.request, gettext("Data updated successfully"))

        if self.request.htmx:
            self.template_name = "widgets/donation_widget/donation_widget_config_update_content.html"
        else:
            self.template_name = "widgets/donation_widget/donation_widget_config_update.html"

        return self.render_to_response(self.get_context_data(form=form, donation_widget_config=self.object))


class DonationWidgetConfigDeleteView(LoginRequiredMixin, DeleteView):
    model = DonationWidgetConfig

    def form_valid(self, form):
        if self.object.donation_widget.user != self.request.user:
            return HttpResponseForbidden()
        donation_widget_id = self.object.donation_widget_id
        self.object.delete()
        messages.success(self.request, gettext("Data deleted successfully"))
        success_url = reverse_lazy("donation_widgets_update", kwargs={"pk": donation_widget_id})
        return HttpResponseLocation(success_url, target="main")


class DonationWidgetLinkView(RedirectView):
    pattern_name = "donation_widgets_update"

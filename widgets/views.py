from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, UpdateView, RedirectView, FormView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from widgets.forms import (
    DonationWidgetForm,
    CreateDonationWidgetForm,
    DonationWidgetConfigFormSet,
    DonationWidgetConfigUpdateForm,
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

    def post(self, request, *args, **kwargs):
        if request.user.donation_widgets.count() >= 3:
            messages.error(request, _("You cannot create more than 3 widgets"))
            return redirect("donation_widgets_list")
        return super().post(request, *args, **kwargs)


class DonationWidgetUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "widgets/donation_widget/donation_widget_update.html"
    model = DonationWidget
    context_object_name = "donation_widget"
    form_class = DonationWidgetForm

    def get_queryset(self):
        return self.model.objects.prefetch_related("configs")

    def form_valid(self, form):
        if self.object.user != self.request.user:
            return HttpResponseForbidden()
        self.object = form.save()
        return self.render_to_response(self.get_context_data(form=form, donation_widget=self.object))


class DonationWidgetDeleteView(LoginRequiredMixin, MultipleObjectMixin, DeleteView):
    model = DonationWidget
    success_url = reverse_lazy("donation_widgets_list")
    context_object_name = DonationWidgetListView.context_object_name
    template_name = "widgets/donation_widget/donation_widget_list_content.html"

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user).order_by("id")

    def form_valid(self, form):
        if self.object.user != self.request.user:
            return HttpResponseForbidden()
        self.object.delete()
        object_list = self.get_queryset()
        context = self.get_context_data(object_list=object_list)
        return self.render_to_response(context)


class DonationWidgetConfigUpdateView(LoginRequiredMixin, UpdateView):
    model = DonationWidgetConfig
    form_class = DonationWidgetConfigUpdateForm
    context_object_name = "donation_widget_config"
    template_name = "widgets/donation_widget/donation_widget_config_update.html"


class DonationWidgetLinkView(RedirectView):
    pattern_name = "donation_widgets_update"

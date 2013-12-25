# django imports
from django import forms
from django.db import models
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

# django-portlets imports
from portlets.models import Portlet


class Subscriber(models.Model):
    """
    Somebody who describes to a newsletter.
    """
    email = models.EmailField(_(u"E-mail"))
    creation_date = models.DateTimeField(_(u"Creation date"), auto_now_add=True)
    modification_date = models.DateTimeField(_(u"Modification date"), auto_now=True, auto_now_add=True)
    active = models.BooleanField(_(u"Active"), default=True)


class SubscriberPortlet(Portlet):
    """
    Portlet to collect subscribers.
    """

    limit = models.IntegerField(blank=True, null=True)

    def render(self, context):
        return render_to_string("lfc_newsletter/newsletter_portlet.html", {})

    def form(self, **kwargs):
        return SubscriberPortletForm(instance=self, **kwargs)


class SubscriberPortletForm(forms.ModelForm):
    """Form to add / edit an SubscriberPortlet.
    """
    class Meta:
        model = Subscriber
        fields = ("email")

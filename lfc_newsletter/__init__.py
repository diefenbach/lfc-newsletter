# django imports
from django.utils.translation import ugettext_lazy as _

# portlets imports
from portlets.utils import register_portlet
from portlets.utils import unregister_portlet

# lfc_blog imports
from lfc_newsletter.models import SubscriberPortlet

name = "Newsletter"
description = _(u"A simple newsletter for LFC")


def install():
    """Installs the blog application.
    """
    # Register Portlets
    register_portlet(SubscriberPortlet, "Newsletter")


def uninstall():
    """Uninstalls the blog application.
    """
    # Unregister portlet
    unregister_portlet(SubscriberPortlet)

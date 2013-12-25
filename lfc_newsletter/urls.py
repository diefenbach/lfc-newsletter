# django imports
from django.conf.urls.defaults import *

urlpatterns = patterns('lfc_newsletter.views',
    url(r'^add-subscriber$', 'add_subscriber', name="lfc_newsletter_add_subscriber"),
)

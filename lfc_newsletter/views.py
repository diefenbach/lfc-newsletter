# python imports
import urllib
import urlparse

# django imports
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect

# lfc_newsletter imports
from lfc_newsletter.models import Subscriber
from lfc_newsletter.models import SubscriberForm


@require_POST
def add_subscriber(request, template_name="lfc_newsletter/add_subscriber.html"):
    form = SubscriberForm(data=request.POST)
    if form.is_valid():
        Subscriber.objects.get_or_create(email=form.cleaned_data.get("email"))
        message = "1"
    else:
        message = "0"

    url = request.META.get("HTTP_REFERER", "/")
    parsed = urlparse.urlparse(url)
    params = dict(urlparse.parse_qsl(parsed.query))
    params["msg"] = message
    url = "%s://%s%s?%s" % (parsed[0], parsed[1], parsed[2], urllib.urlencode(params))

    return HttpResponseRedirect(url)

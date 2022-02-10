import logging

from django.shortcuts import render

from .models import Profile

_logger = logging.getLogger(__name__)


def about_me_index(request):
    _logger.info(request)
    profiles = Profile.objects.all()
    _logger.info(profiles)
    return render(
        request=request,
        template_name="about_me_index.html",
        context=dict(profiles=profiles),
    )
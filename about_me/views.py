from django.shortcuts import render

from .models import CurriculumVitae


def about_me_index(request):
    curriculums = CurriculumVitae.objects.all()
    return render(
        request=request,
        template_name="about_me_index.html",
        context=dict(curriculums=curriculums),
    )
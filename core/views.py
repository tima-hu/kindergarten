from django.shortcuts import render

from .models import Kindergarten, Teacher


def index(request):
    return render(request, "index.html", {
        "k": Kindergarten.objects.first(),
        "teachers": Teacher.objects.filter(is_active=True),
    })

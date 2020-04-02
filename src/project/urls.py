from pathlib import Path

from django.contrib import admin
from django.http import HttpResponse
from django.urls import path


here = Path(__file__).parent.resolve()


def view1(r):
    index = here.parent.parent / "index.html"
    with index.open() as f:
        return HttpResponse(f.read())


def view2(r):
    index = here.parent.parent / "contact.html"
    with index.open() as f:
        return HttpResponse(f.read())


def view3(r):
    index = here.parent.parent / "education.html"
    with index.open() as f:
        return HttpResponse(f.read())


def view4(rb):
    index = here.parent.parent / "head.css"
    with index.open("rb") as f:
        return HttpResponse(f.read(), content_type="text/css")


def view5(rb):
    index = here.parent.parent / "IMG_me.jpg"
    with index.open("rb") as f:
        return HttpResponse(f.read(), content_type="image/jpg")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index.html', view1),
    path('contact.html', view2),
    path('education.html', view3),
    path('head.css', view4),
    path('', view1),
    path('IMG_me.jpg', view5),
]

from pathlib import Path

from django.contrib import admin
from django.conf import settings
from django.http import HttpResponse
from django.urls import path
from django.shortcuts import render

#here = Path(__file__).parent.resolve()
#head = here.parent.parent / "head.css"
#IMG_me = here.parent.parent / "IMG_me.jpg"


#def read_static(fn, ct):
  #  with fn.open("rb") as src:
     #   content = src.read()
      #  resp = HttpResponse(content, content_type=ct)
        #return resp


#def view4(rb, f=read_static):
    #return f(head, "text/css")


#def view5(rb, f=read_static):
   # return f(IMG_me, "image/jpg")


def view1(req):
    return render(req, "index.html")


def view2(req):
    return render(req, "contact.html")


def view3(req):
    return render(req, "education.html")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index.html', view1),
    path('contact.html', view2),
    path('education.html', view3),
    path('', view1),
]


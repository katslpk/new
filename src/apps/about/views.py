from django.shortcuts import render


def view1(req):
    return render(req, "about/index.html")
from django.shortcuts import render


def view2(req):
    return render(req, "contact/index.html")


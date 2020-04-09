from django.shortcuts import render


def view3(req):
    return render(req, "education/index.html")

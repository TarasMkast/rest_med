from django.shortcuts import render


def handler404(request, exception):
    return render(request, "404.html", context={})


def handler500(request):
    return render(request, "404.html", context={})

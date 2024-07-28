from django.shortcuts import render


def temporary(request):
    return render(request, "base.html")

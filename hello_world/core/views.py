from django.shortcuts import render

def index(request):
    return render(
        request,
        "index.html",
        {
            "title": "IMAGINE",
        },
    )

def eogrenme(request):
    return render(
        request,
        "e-ogrenme.html",
        {
            "title": "E-ÖĞRENME",
        },
    )

def haberler(request):
    return render(
        request,
        "haberler.html", 
        {
            "title": "HABERLER",
        },
    )

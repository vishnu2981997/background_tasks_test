from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, "multi_processing_test/home.html", {})

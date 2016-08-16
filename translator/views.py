from django.shortcuts import render


# Define the main view, which will serve up a AngularJS SPA
def index(request):
    return render(request, "translator/index.html")

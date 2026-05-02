from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html') # El fichié hédha elli fih el carousel w les annonces
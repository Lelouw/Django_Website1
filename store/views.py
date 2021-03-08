from django.shortcuts import render

# Create your views here.
def store(request):
    contex = {}
    return render(request, 'store/store.html', contex)

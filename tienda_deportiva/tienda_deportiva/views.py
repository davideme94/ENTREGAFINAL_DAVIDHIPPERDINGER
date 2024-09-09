from django.shortcuts import render
def homepage(request):
    return render(request,"homepage.html")

def indumentaria(request):
    return render(request, "indumentaria.html")


def about(request):
    return render(request, 'aboutpage.html')

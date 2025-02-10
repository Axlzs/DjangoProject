from django.shortcuts import render
#from django.http import HttpResponse

def homepage(request):
    #return HttpResponse("Hello world!")
    return render(request, 'home.html')
    
def about(request):
    #return HttpResponse("About page")
    return render(request, 'about.html')
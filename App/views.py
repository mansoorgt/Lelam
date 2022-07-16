from django.shortcuts import render

# Create your views here.
def RenderSide(request):
    return render(request,'MainCard.html')
def Events(reqeust):
    return render(reqeust,'Events.html')    
def Tradepage(request):
    return render(request,'Trade.html')    
from django.shortcuts import render

def index(request):

    return render(request,'tail_core/index.html')
from django.shortcuts import render

def showIndex(request):
    data={"name":"siddhu","salary":25000}
    return render (request,"index.html",data)
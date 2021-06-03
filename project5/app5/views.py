from django.shortcuts import render

def showIndex(request):
    emp_info = {"idno":101,"name":"siddhu","salary":25000}
    return render(request,"main.html",emp_info)
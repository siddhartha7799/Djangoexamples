from django.shortcuts import render

def showIndex(request):
    return render(request,"index.html")

def loginCheck(request):

    if request.method == "POST":
        username=request.POST.get("t1")
        password = request.POST.get("t2")
        if username== "ravi " and password=="ravi1234@":
            return render(request,"index.html",{"admin":"welcome"})
        elif username=="ravi" and password=="kumar@123":
            return render(request,"Index.html",{"employee":"welcome"})
        elif username=="ravi" and password=="ravikumar@123":
            return render(request,"index.html",{"customer":"welcome"})
        else:
            return render(request,"index.html",{"message":"error"})
    if request.method =="GET":
        return render(request,"index.html")

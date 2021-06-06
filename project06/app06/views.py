from django.shortcuts import render

def showIndex(request):
    students_info = {"data":
                         [
                             {"idno":101,"name":"siddhartha","marks":[65,35,19,65,73,40]},
                             {"idno":102,"name":"ranjith","marks": [60,65,75,21,45,60]},
                             {"idno":103,"name": "tharun","marks": [68,54,31,87,44,65]},
                             {"idno":104,"name": "imran","marks": [35,45,66,76,36,"ab"]},
                             {"idno":105,"name": "akhilesh","marks": [66,76,35,22,57,82]},
                         ]
                    }
    return render(request,"marks.html",students_info)

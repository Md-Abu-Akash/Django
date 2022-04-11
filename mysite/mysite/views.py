from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    return render(request,'index.html')

# def about(request):
#     djtext =request.GET.get('text', 'default')
#     dic={'name':djtext[0].upper
#         ,'list':['one','two','three']}
#     return render(request,'about.html',dic)

def components(request):
    return render(request,'components.html')

def signUp(request):
    try:
        fname= request.POST.get('fname')
        lname = request.POST.get('lname')
        print(fname + lname)

    except:
        pass
    return render(request,'signUp.html')
from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'a':50}
    return render(request,'condition.html',d)

def condition1(request):
    d={'a':50}
    return render(request,'condition1.html',d)

def condition2(request):
    d={'a':150,'b':100}
    return render(request,'condition2.html',d)

def condition3(request):
    d={'a':50,'b':1000,'c':200}
    return render(request,'condition3.html',d)

def condition4(request):
    d={'a':50,'b':100,'c':200,'d':40}
    return render(request,'condition4.html',d)
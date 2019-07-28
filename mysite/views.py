

from django.shortcuts import HttpResponse,render
def home(request):
    return HttpResponse("hello django")

def about(request):
    h ="""
    <!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>My First Heading</h1>
<p>My first paragraph.</p>

</body>
</html>
    """
    j="hello"
    return HttpResponse(h)


def index(request):
    a=100
    b="hello"

    l=[3,5,7,8,"Verma","Raja"]
    d={
        'a':a,
        'b':b,
        'l':l,
    }
    return render(request,'index.html',d)


def test(request):
    c=None
    if request.method=='POST':
        a =request.POST.get('t1')
        b =request.POST.get('t2')
        # c=int(a)+int(b)
        if int(a)==int(b):
            c="Equal Vales"
        else:
            c="Un-Equal"
    d={
      'c':c
    }
    return render(request,'test.html',d)


def myform(request):
    myt1=None
    if request.method=='GET':
        myt1 =request.GET.get('t1')

    context ={
        't1':myt1,
    }
    return render(request,'form.html',context)
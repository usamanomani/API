from django.shortcuts import render,HttpResponse,redirect
from .form import DemoForm,Userform
from rest_framework import viewsets
from .models import Users
from .api_serializer import UsersSerializer
# Create your views here.
def test (request):
    name=""
    if request.method=='POST':
        name =request.POST.get('name')
        print(name)

    context={
        'name':name
    }
    # return HttpResponse('Hello')
    return render(request,'test_app.html',context)



def dform_text (request):
    name=""
    color="#ddd"
    form =DemoForm(request.POST or None)

    if form.is_valid():
        name =form.cleaned_data.get('name')
        email =form.cleaned_data.get('email')
        color =form.cleaned_data.get('color')
        print(name,email,color)
        return redirect('')
        # name =request.POST.get('name')

    context={
        'name':name,
        'form':form,
        'color':color
    }
    # return HttpResponse('Hello')
    return render(request,'dform.html',context)


def add_user(request):
    if request.method=='POST':
        fname =request.POST.get('fname')
        mobile =request.POST.get('mobile')
        email =request.POST.get('email')
        address =request.POST.get('address')
        print(fname,mobile,email,address)

        u =Users()
        u.fname=fname
        u.mobile=mobile
        u.email=email
        u.address=address

        u.save()
        print('save ho gya')
    # allUser =Users.objects.all()
    allUser =Users.objects.all()
    data ={
        'allUser':allUser
    }

    return render(request,'add-users.html',data)


def form_save_user(request):
    form =Userform(request.POST or None)
    if form.is_valid():
        form.save()
    context ={
        'form':form
    }
    return render(request,'form_save_user.html',context)



class UserViewApi(viewsets.ModelViewSet):

    queryset = Users.objects.all()
    serializer_class = UsersSerializer
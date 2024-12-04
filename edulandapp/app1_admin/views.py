from django.shortcuts import render
from django.http import HttpResponse
from app1_admin.models import Mainpage
from app1_admin.forms import AForm
# Create your views here.
def print(request):
    return HttpResponse("hello its a app1")

def load(request):
    return render(request,'index.html')

def list(request):
    listview=Mainpage.objects.all()
    return render(request,'list.html',{'listview':listview})

def adddata(request):
    if request.POST:
        add=AForm(request.POST)
        if add.is_valid():
         add.save()
    else:
        add=AForm()
    return render(request,'add.html',{'added':add})
    


def edit(request,pk):
    edited=Mainpage.objects.get(pk=pk)
    if request.POST:
        editfrm=AForm(request.POST,instance=edited)
        if editfrm.is_valid():
            edited.save()
    else:
        editfrm=AForm(instance=edited)
    return render(request,'add.html',{'added':editfrm})


def delete(request,pk):
    deleted=Mainpage.objects.get(pk=pk)
    deleted.delete()
    sdeleted=Mainpage.objects.all()
    return render(request,'list.html',{'listview':sdeleted})

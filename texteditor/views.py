from django.shortcuts import render
from .forms import EditorForm
def index(request):
    form=EditorForm()
    a=5
    b=a
    return render(request,'index.html',{'form':form})
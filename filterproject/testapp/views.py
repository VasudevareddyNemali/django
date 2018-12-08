from django.shortcuts import render
from testapp.models import FilterModel

def upper_view(request):
    disp_dict=FilterModel.objects.all()
    return render(request,'testapp/upper.html',{'disp_dict':disp_dict})

def lower_view(request):
    disp_dict=FilterModel.objects.all()
    return render(request,'testapp/lower.html',{'disp_dict':disp_dict})

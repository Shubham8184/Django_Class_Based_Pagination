from django.shortcuts import redirect, render
from .models import Laptop
from .forms import Laptopform
from django.core.paginator import Paginator
from django.views.generic import ListView


def Addlaptopview(request):
    form=Laptopform()
    if request.method == 'POST':
        form=Laptopform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listing')
    template_name='Pagination/Addorder.html'
    context={'form':form}
    return render(request,template_name,context)

def Showlaptopview(request):
    ord=Laptop.objects.all()
    template_name='Pagination/Showorder.html'
    context={'ord':ord}
    return render(request,template_name,context)

def Updatelaptopview(request,update):
    lap=Laptop.objects.get(id=update)
    form=Laptopform(instance=lap)
    if request.method == 'POST':
        form=Laptopform(request.POST,instance=lap)
        if form.is_valid():
            form.save()
            return redirect('showlaptop')
    template_name='Pagination/Addorder.html'
    context={'form':form}
    return render(request,template_name,context)

def Deletelaptopview(request,delete):
    lap=Laptop.objects.get(id=delete)
    lap.delete()
    return redirect('showlaptop')

class listing(ListView):
    model=Laptop
    paginate_by=5
    template_name='Pagination/Showorder.html'
    

def Homeview(request):
    template_name='Pagination/Home.html'
    return render(request,template_name)

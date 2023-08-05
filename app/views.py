from django.shortcuts import render, redirect
from .models import Employee
from django.core.paginator import Paginator

# Create your views here.


def INDEX(request):
    employee = Employee.objects.all().order_by("-id")
    
    #pagination
    paginator = Paginator(employee, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    n=page_obj.end_index()-page_obj.start_index() + 1
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        addemployee = Employee(
            name=name,
            email=email,
            address = address,
            phone = phone,
        )  
        addemployee.save()
        return redirect('index')
    
    
 
    
    context ={
        'employee':page_obj,
        'n':n,
    }

    return render(request, "app/index.html", context)



def delete_emp(request, pk):
    if request.method == "POST":
        emp = Employee.objects.get(pk=pk)
        emp.delete()
    return redirect('index')


def delete_multiple(request, *args, **kwargs):
    if request.method == "POST":
        emp_ids = request.POST.getlist('id[]')
        for i in emp_ids:
            if i == 'on':
                continue
            emp = Employee.objects.get(pk=i)
            emp.delete()
        return redirect('index')
    return redirect('index')

def edit_emp(request, pk):
    emp = Employee.objects.get(pk=pk)
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        emp.name = name
        emp.email = email
        emp.address = address
        emp.phone = phone
        emp.save()
    return redirect('index')


        
        
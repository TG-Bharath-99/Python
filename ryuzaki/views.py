from django.shortcuts import render,redirect
from . models import Employee

def index(request):
    return render(request, 'index.html')

def emp_details(request):
    emp_data = Employee.objects.all()
    emp_dict = {'emp_list': emp_data}
    return render(request, 'display.html', emp_dict)

def add_employee(request):
    if request.method == 'POST':
        Employee.objects.create(
            name=request.POST['name'],
            eid=request.POST['eid'],
            address=request.POST['address'],
            salary=request.POST['salary'])
        return redirect('employees')
    return render(request, 'add.html')

def update_employee(request, id):
    e = Employee.objects.get(eid=id)
    if request.method == 'POST':
        e.name = request.POST['name']
        e.eid = request.POST['eid']
        e.address = request.POST['address']
        e.salary = request.POST['salary']
        e.save()
        return redirect('employees')
    return render(request, 'update.html', {'e': e})

def delete_employee(request, id):
    e = Employee.objects.get(eid=id)
    if request.method == 'POST':
        e.delete()
        return redirect('employees')
    return render(request, 'delete.html', {'e': e})
from django.shortcuts import render

from .forms import EmployeeForms
# Create your views here.

def employee_register(request):
    if request.method =='POST':
        form = EmployeeForms(request.POST)

        if form.is_valid():
            form.save()

        return render(request, "success.html")
    else:
        form = EmployeeForms()

        return render(request, "employee_register.html", {'form': form})
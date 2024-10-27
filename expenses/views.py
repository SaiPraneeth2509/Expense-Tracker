from django.shortcuts import render,redirect,get_object_or_404
from .forms import ExpenseForm
# Create your views here.
from .models import Expense

def add_expense(request):
    if request.method=='POST':
        form=ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    
    return render(request,'expenses/add_expense.html',{'form':form})

def expense_list(request):
    expenses= Expense.objects.all()
    return render(request,'expenses/expense_list.html',{'expenses':expenses})

def edit_expense(request,pk):
    expense = get_object_or_404(Expense,pk=pk)
    if request.method=='POST':
        form = ExpenseForm(request.POST,instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form=ExpenseForm(instance=expense)
    return render(request,'expenses/edit_expense.html',{'form':form})

def delete_expense(request,pk):
    expense=get_object_or_404(Expense,pk=pk)
    if request.method=='POST':
        expense.delete()
        return redirect('expense_list')
    return render(request,'expenses/delete_expense.html',{'expense':expense})


    print("Template Directories:", settings.TEMPLATES[0]['DIRS'])
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Department, Term, Banji
from .forms import DepartmentForm, TermForm
# Create your views here.


def index(request):
    return HttpResponse("这是预想中的设置中心")


def department_index(request):
    departments = Department.objects.all()
    return render(request, 'department/index.html', {'departments': departments})


def department_create(request):
    form = DepartmentForm()
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, request.POST.get('title')+"内容已被添加，操作成功！")
            return redirect(reverse('setting:department-index'))
    return render(request, 'department/create.html', {'form': form})


def department_edit(request, ids):
    department = get_object_or_404(Department, pk=ids)
    if request.method == 'POST':
        form = DepartmentForm(data=request.POST, instance=department)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, department.title+"设置已被修改，操作成功！")
            return redirect(reverse('setting:department-index'))
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'department/edit.html', {'form': form, 'department': department})


def department_del(request, ids):
    department = get_object_or_404(Department, pk=ids)
    department.delete()
    return redirect(reverse('setting:department-index'))


def term_index(request):
    terms = Term.objects.all()
    return render(request, 'term/index.html', {'terms': terms})


def term_create(request):
    form = TermForm()
    if request.method == 'POST':
        form = TermForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '新增学期成功！')
            return redirect(reverse('setting:term-index'))
    return render(request, 'term/create.html', {'form': form})


def term_edit(request, ids):
    term = get_object_or_404(Term, pk=ids)
    form = TermForm(instance=term)
    if request.method == 'POST':
        form = TermForm(data=request.POST, instance=term)
        if form.is_valid():
            form.save()
            messages.success(request, term.title+'-数据修改成功!')
            return redirect(reverse('setting:term-index'))
    return render(request, 'term/edit.html', {'form': form, 'term': term})


def term_del(request, ids):
    term = get_object_or_404(Term, pk=ids).delete()
    messages.success(request, term.title+' 已被成功删除！')
    return redirect(reverse('setting:term-index'))

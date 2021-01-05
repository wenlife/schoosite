from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse, HttpRequest
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Teacher, TeacherImport
from .forms import TeacherForm, TeacherImportForm
import pandas as pd
# Create your views here.


def teacher_index(request):
    teachers = Teacher.objects.all().order_by('pinx')
    search = ""
    if request.GET.get('search'):
        search = request.GET.get('search')
        teachers = Teacher.objects.filter(pinx__contains=search)
        search = "&search="+search
    p = Paginator(teachers, 15, orphans=True)
    page = p.get_page(request.GET.get('page'))
    path = HttpRequest.get_full_path(self=request)
    return render(request, 'teacher/index.html', {'teachers': teachers, 'page': page, 'search': search, 'path': path})


def teacher_create(request):
    form = TeacherForm()
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '新增教师成功！')
            return redirect(reverse('guest:teacher_index'))
    return render(request, 'teacher/create.html', {'form': form})


def teacher_import(request):
    form = TeacherImportForm()
    if request.method == 'POST':
        form = TeacherImportForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save()
            print(f.file.path)
            book = pd.read_excel(f.file.path, sheet_name=0)
            book = book.fillna("")
            #all_data = book.head(5).T.to_dict()
            all_data = book.to_dict(orient='records')
            # t_list = list()
            # for s in all_data:
            #     print(s)
            #     t = Teacher(**s)
            #     t_list.append(t)
            t_list = [Teacher(**s) for s in all_data]
            Teacher.objects.bulk_create(t_list)
            #t = Teacher()
            #t.save()
            #print(book.head(5).T.to_dict())

            f.delete()

    return render(request, 'teacher/import.html', {'form': form})


def teacher_edit(request, ids):
    teacher = get_object_or_404(Teacher, pk=ids)
    form = TeacherForm(instance=teacher)
    if request.method == 'POST':
        form = TeacherForm(data=request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            messages.success(request, '教师'+teacher.name+'信息修改成功！')
            return redirect(reverse('guest:teacher_index'))
    return render(request, 'teacher/edit.html', {'form': form, 'teacher':teacher})


def teacher_del(request, ids):
    path = request.GET.get('path')
    teacher = get_object_or_404(Teacher, pk=ids)
    teacher.delete()
    messages.success(request, '教师<'+teacher.name+">删除成功！")
    if path:
        print(path)
        return redirect(path)
    else:
        return redirect(reverse('guest:teacher_index'))

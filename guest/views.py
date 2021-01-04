from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse
from .models import Teacher, TeacherImport
from .forms import TeacherForm, TeacherImportForm
import pandas as pd
# Create your views here.


def teacher_index(request):
    teachers = Teacher.objects.all()
    if request.method == 'POST':
        search = request.POST.get('table_search')
        teachers = Teacher.objects.filter(pinx__contains=search)
    return render(request, 'teacher/index.html', {'teachers': teachers})


def teacher_create(request):
    form = TeacherForm()
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
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
            return redirect(reverse('guest:teacher_index'))
    return render(request, 'teacher/edit.html', {'form': form, 'teacher':teacher})


def teacher_del(request, ids):
    teacher = get_object_or_404(Teacher, pk=ids)
    teacher.delete()
    return redirect(reverse('guest:teacher_index'))

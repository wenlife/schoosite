from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse
from .models import Teacher, TeacherImport
from .forms import TeacherForm, TeacherImportForm
import xlrd
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
            #print(form.cleaned_data.get('file').path)
            f = form.save()
            #files = TeacherImport.objects.all().delete()
            print(f.file.path)
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

from django import forms
from .models import Teacher


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'pinx', 'subject', 'type', 'gender', 'graduate']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'pinx': forms.TextInput(attrs={'class': 'form-control'}),
            'subject': forms.Select(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'graduate': forms.TextInput(attrs={'class': 'form-control'})
        }
        labels = {
            'name': '姓名',
            'pinx': '拼写',
            'subject': '任教科目',
            'type': '类型',
            'gender': '性别',
            'graduate': '毕业学校'
        }
        help_texts = {
            'name': '请输入教师的真实姓名',
            'pinx': '输入教师姓名的全拼，正确输入有利于快速找到该老师',
            'subject': '该教师的任教科目，可以为空',
            'type': '该教师的类型',
            'gender': '请选择教师性别，如有其他选项请告知',
            'graduate': '请输入该教师的最高学历的毕业学校'
        }
        error_messages = {
            'gender': {'invalid': '格式不正确'}
        }


class TeacherImport(forms.Form):
    file = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}), label='选择文件',)


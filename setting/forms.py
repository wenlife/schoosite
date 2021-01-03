from django import forms
from setting.models import Department

# class DepartmentForm(forms.Form):
#     title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'special'}))
#     entry_year = forms.CharField(max_length=4)
#     person_in_charge = forms.CharField(max_length=40)
#     note = forms.CharField(max_length=100)


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['title', 'entry_year', 'person_in_charge', 'note']
        widgets = {
          'title': forms.TextInput(attrs={'class': 'form-control'}),
          'entry_year': forms.TextInput(attrs={'class': 'form-control'}),
          'person_in_charge': forms.TextInput(attrs={'class': 'form-control'}),
          'note': forms.TextInput(attrs={'class': 'form-control'})
        }
        labels = {
            'title': "标题",
            'entry_year': "入学年份",
            'person_in_charge': '负责人',
            'note': '备注'

        }
        help_texts = {
            'title': '标题内容为教学部的名字',
            'entry_year': '请输入当前管理年级的入学年份，将决定可以管理到哪个年级的数据',
            'person_in_charge': '年级当前负责人，用于教师分辨自己所属年级',
            'note': '其他需要注明的信息'
        }

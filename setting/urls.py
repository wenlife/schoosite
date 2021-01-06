from django.urls import path
from . import views
app_name = 'setting'
urlpatterns = [
    path('department/', views.department_index, name='department-index'),
    path('department_create/', views.department_create, name='department-create'),
    path('department_edit/<int:ids>', views.department_edit, name='department-edit'),
    path('department_del/<int:ids>', views.department_del, name='department-del'),
    path('term/', views.term_index, name='term-index'),
    path('term/create/', views.term_create, name='term-create'),
    path('term/edit/<int:ids>', views.term_edit, name='term-edit'),
    path('term/del/<int:ids>', views.term_del, name='term-del')
]

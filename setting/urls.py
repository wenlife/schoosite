from django.urls import path
from . import views
app_name = 'setting'
urlpatterns = [
    path('department/', views.department_index, name='department-index'),
    path('department_create/', views.department_create, name='department-create'),
    path('department_edit/<int:ids>', views.department_edit, name='department-edit'),
    path('department_del/<int:ids>', views.department_del, name='department-del')
]

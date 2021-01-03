from django.urls import path
from . import views
app_name = 'guest'
urlpatterns = [
    path('teacher/', views.teacher_index, name='teacher_index'),
    path('teacher/create', views.teacher_create, name='teacher_create'),
    path('teacher/edit/<int:ids>', views.teacher_edit, name='teacher_edit'),
    path('teacher/del/<int:ids>', views.teacher_del, name='teacher_del'),
    path('teacher/import/', views.teacher_import, name='teacher_import'),

]

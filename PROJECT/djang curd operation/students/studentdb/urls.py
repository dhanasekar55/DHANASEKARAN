from django.urls import path
from .views import home, add_student, edit_student, delete_student

urlpatterns = [
    path('', home, name='home'),
    path('add/', add_student, name='add_student'),
    path('edit/<int:student_id>/', edit_student, name='edit_student'),
    path('delete/<int:student_id>/', delete_student, name='delete_student'),
]
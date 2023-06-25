from django.contrib import admin
from . models import Student
# Register your models here.

@admin.register(Student)
class StuedntAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'department', 'student_id', 'enrolled_in']
    list_filter = ['student_id', 'enrolled_in']
    search_fields = ['first_name', 'last_name', 'department']
 
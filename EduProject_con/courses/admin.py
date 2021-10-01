from django.contrib import admin
from . models import Course
# Register your models here.
#admin.site.register(Course)
#Decorator for Courses Add for Teacher
@admin.register(Course)
#CourseAdmin admin içindeki ModelAdmini extend(miras alır) eder.
#Course için Admin panelini özelleştirme işlemleri
class CourseAdmin(admin.ModelAdmin):
    list_display=('name','available')
    list_filter=('available',)
    search_fields=('name','desc')

from django.shortcuts import render
from .models import Course

def courses_list(req):
    courses=Course.objects.all().order_by('-date')
    #direct returnle göndereceğiz ve daha sonraki eklemeler için dict yapısında gönderiyorum.
    context={
        'courses':courses
    }
    return render(req,'courses.html',context)

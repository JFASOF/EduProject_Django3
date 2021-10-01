from django.urls import path
from . import views #olduğu yerdeki views çağırmak "." kullanılır.

urlpatterns = [
    #path(route,view,opt(kısayol ismi))
    path('', views.courses_list,name="courses"),
]
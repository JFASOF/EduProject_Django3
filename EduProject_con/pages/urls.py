from django.urls import path
from . import views #olduğu yerdeki views çağırmak "." kullanılır.

urlpatterns = [
    #path(route,view,opt(kısayol ismi))
    path('', views.index,name="index"),
    path('about/', views.about,name="about"),
]
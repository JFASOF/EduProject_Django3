from django.db import models

#classlar bir tablodur
class Course(models.Model):
    name=models.CharField(max_length=200,unique=True,verbose_name="Kurs Adı :",help_text="Bu Kursun Adını Giriniz.")
    desc=models.TextField(blank=True,null=True,verbose_name="Kurs Açıklaması :")#blank son kullanıcı null programsal olarak
    image=models.ImageField(verbose_name="Kurs Görseli:",upload_to="courses/%Y/%m/%d/",default="courses/default_course.jpg")
    date=models.DateTimeField(auto_now=True)#her değişiklik update olarak tarih içinde olsun.
    available=models.BooleanField(verbose_name="Kurs Erişimi:",default=True)

    def __str__(self):
        return self.name
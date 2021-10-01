# Generated by Django 3.2.5 on 2021-07-16 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='available',
            field=models.BooleanField(default=True, verbose_name='Kurs Erişimi:'),
        ),
        migrations.AlterField(
            model_name='course',
            name='desc',
            field=models.TextField(blank=True, null=True, verbose_name='Kurs Açıklaması :'),
        ),
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(default='courses/default_course.jpg', upload_to='courses/%Y/%m/%d/', verbose_name='Kurs Görseli:'),
        ),
    ]
# Generated by Django 4.1.4 on 2023-03-27 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_first_name', models.CharField(max_length=200)),
                ('student_last_name', models.CharField(max_length=100)),
                ('student_class', models.CharField(max_length=150)),
                ('student_address', models.CharField(max_length=160)),
                ('student_school', models.TextField()),
                ('student_email', models.EmailField(max_length=100)),
                ('student_age', models.CharField(max_length=20)),
                ('student_result', models.CharField(max_length=100)),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField()),
            ],
        ),
    ]
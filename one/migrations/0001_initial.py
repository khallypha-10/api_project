# Generated by Django 4.2.2 on 2023-06-24 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=70)),
                ('last_name', models.CharField(max_length=70)),
                ('student_id', models.IntegerField()),
                ('department', models.CharField(max_length=150)),
                ('enrolled_in', models.DateField(auto_now_add=True)),
            ],
        ),
    ]

# Generated by Django 4.1.2 on 2022-10-22 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teatru', '0003_employee_department_alter_employee_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='show_pics')),
            ],
        ),
    ]

# Generated by Django 2.2.1 on 2019-12-17 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('contact', models.IntegerField(unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=40)),
                ('status', models.CharField(max_length=30)),
                ('doj', models.DateField(auto_now_add=True)),
            ],
        ),
    ]

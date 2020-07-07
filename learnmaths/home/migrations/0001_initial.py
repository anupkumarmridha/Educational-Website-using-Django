# Generated by Django 3.0.6 on 2020-06-16 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=125)),
                ('email', models.CharField(max_length=125)),
                ('phone', models.CharField(max_length=13)),
                ('desc', models.TextField(max_length=125)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
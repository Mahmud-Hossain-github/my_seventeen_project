# Generated by Django 2.2.5 on 2019-10-15 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20191015_0213'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]

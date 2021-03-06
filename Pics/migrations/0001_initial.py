# Generated by Django 3.1.2 on 2020-10-12 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categories', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=400, null=True)),
                ('descripton', models.TextField(blank=True, max_length=400, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Polygon/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pics.categories')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pics.location')),
            ],
        ),
    ]

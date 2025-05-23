# Generated by Django 5.1.7 on 2025-04-22 10:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('origin', models.CharField(max_length=100)),
                ('manufacturing_since', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='PhoneModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=100)),
                ('launch_date', models.DateField()),
                ('platform', models.CharField(max_length=50)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PhoneReview.brand')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_article', models.TextField()),
                ('date_published', models.DateField(auto_now_add=True)),
                ('phone_models', models.ManyToManyField(to='PhoneReview.phonemodel')),
            ],
        ),
    ]

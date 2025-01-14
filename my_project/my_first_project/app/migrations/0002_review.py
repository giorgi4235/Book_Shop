# Generated by Django 5.0.7 on 2024-07-22 16:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_text', models.TextField()),
                ('rating', models.IntegerField()),
                ('reviewer_name', models.CharField(max_length=100)),
                ('review_date', models.DateField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='app.book')),
            ],
        ),
    ]

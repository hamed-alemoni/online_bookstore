# Generated by Django 3.2.5 on 2021-08-21 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0012_educationyear'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_education_year',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='book_education_year', to='Book.educationyear'),
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.IntegerField(default=None),
        ),
    ]

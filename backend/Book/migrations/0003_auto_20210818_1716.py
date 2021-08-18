# Generated by Django 3.2.5 on 2021-08-18 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0002_auto_20210816_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('d', 'Draft'), ('p', 'Published')], default=None, max_length=1),
        ),
        migrations.AlterField(
            model_name='book',
            name='international_standard_book_number',
            field=models.CharField(max_length=13),
        ),
    ]

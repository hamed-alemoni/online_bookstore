# Generated by Django 3.2.5 on 2021-08-18 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0004_alter_book_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('d', 'Draft'), ('p', 'Published')], max_length=1),
        ),
    ]

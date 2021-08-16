# Generated by Django 3.2.5 on 2021-08-16 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Publisher',
            new_name='BookPublisher',
        ),
        migrations.RemoveField(
            model_name='book',
            name='publisher',
        ),
        migrations.AddField(
            model_name='book',
            name='book_publisher',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='book_publishers', to='Book.bookpublisher'),
        ),
        migrations.AddField(
            model_name='book',
            name='book_subject',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='book_subjects', to='Book.booksubject'),
        ),
        migrations.AddField(
            model_name='book',
            name='book_type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='book_types', to='Book.booktype'),
        ),
    ]
# Generated by Django 4.2.3 on 2023-07-22 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='discription',
            new_name='activity',
        ),
        migrations.RemoveField(
            model_name='product',
            name='Product_name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.AddField(
            model_name='product',
            name='dates',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='hours',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='mins',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='months',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]

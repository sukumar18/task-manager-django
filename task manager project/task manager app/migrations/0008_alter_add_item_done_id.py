# Generated by Django 4.2.3 on 2023-07-24 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_store', '0007_alter_add_item_done_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_item_done',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

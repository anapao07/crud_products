# Generated by Django 3.0.8 on 2020-07-25 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='cantidad',
            new_name='existencia',
        ),
        migrations.RemoveField(
            model_name='products',
            name='imagen',
        ),
        migrations.AddField(
            model_name='products',
            name='categoria',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]

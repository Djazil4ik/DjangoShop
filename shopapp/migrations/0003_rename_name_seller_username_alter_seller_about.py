# Generated by Django 4.2.11 on 2024-03-25 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0002_product_datetime_product_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seller',
            old_name='name',
            new_name='username',
        ),
        migrations.AlterField(
            model_name='seller',
            name='about',
            field=models.TextField(blank=True),
        ),
    ]
# Generated by Django 3.1.5 on 2021-01-23 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryfrontend', '0007_bookmodel_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookmodel',
            old_name='amount',
            new_name='store_amount',
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='ISBN',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='pages',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

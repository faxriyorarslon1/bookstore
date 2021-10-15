# Generated by Django 3.1.5 on 2021-02-01 11:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('libraryfrontend', '0012_auto_20210131_1049'),
    ]

    operations = [
        migrations.RenameField(
            model_name='authormodel',
            old_name='created_on',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='authormodel',
            old_name='modified_on',
            new_name='modified_at',
        ),
        migrations.RenameField(
            model_name='bookmodel',
            old_name='created_on',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='bookmodel',
            old_name='modified_on',
            new_name='modified_at',
        ),
        migrations.RenameField(
            model_name='categorymodel',
            old_name='created_on',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='categorymodel',
            old_name='modified_on',
            new_name='modified_at',
        ),
        migrations.RenameField(
            model_name='publishermodel',
            old_name='created_on',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='publishermodel',
            old_name='modified_on',
            new_name='modified_at',
        ),
        migrations.RemoveField(
            model_name='authormodel',
            name='deleted',
        ),
        migrations.RemoveField(
            model_name='bookmodel',
            name='deleted',
        ),
        migrations.RemoveField(
            model_name='categorymodel',
            name='deleted',
        ),
        migrations.RemoveField(
            model_name='publishermodel',
            name='deleted',
        ),
        migrations.AddField(
            model_name='authormodel',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='authormodel',
            name='deleted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='authormodel_deletedby', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='deleted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookmodel_deletedby', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='categorymodel',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='categorymodel',
            name='deleted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categorymodel_deletedby', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='publishermodel',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publishermodel',
            name='deleted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='publishermodel_deletedby', to=settings.AUTH_USER_MODEL),
        ),
    ]

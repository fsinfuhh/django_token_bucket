# Generated by Django 2.1.15 on 2019-12-16 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('django_token_bucket', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tokenbucket',
            old_name='user',
            new_name='object_id',
        ),
        migrations.AddField(
            model_name='tokenbucket',
            name='content_type',
            field=models.ForeignKey(null=True,on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
    ]

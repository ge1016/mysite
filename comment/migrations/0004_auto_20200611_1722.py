# Generated by Django 3.0.6 on 2020-06-11 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0003_auto_20200611_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='parent_id',
        ),
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='comment.Comment'),
        ),
    ]

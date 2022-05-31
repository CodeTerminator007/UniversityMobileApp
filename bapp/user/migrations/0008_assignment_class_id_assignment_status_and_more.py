# Generated by Django 4.0 on 2022-04-18 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_assignment_faculty'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='class_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.class'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='assignmentsubmission',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='assignmentsubmission',
            name='marks',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='assignmentsubmission',
            name='submission_datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

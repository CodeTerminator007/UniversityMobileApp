# Generated by Django 4.0 on 2022-04-18 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_assignment_alter_user_profile_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='faculty',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.faculty'),
        ),
    ]
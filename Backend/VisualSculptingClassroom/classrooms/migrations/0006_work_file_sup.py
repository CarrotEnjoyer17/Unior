# Generated by Django 5.0.3 on 2024-03-21 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classrooms', '0005_work_file_model_work_file_textures'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='file_sup',
            field=models.FileField(null=True, upload_to='models'),
        ),
    ]
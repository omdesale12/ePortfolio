# Generated by Django 4.2.4 on 2023-09-01 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_userprofile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(default='default1.jpg', upload_to='profile_pics'),
        ),
    ]

# Generated by Django 4.2.4 on 2023-09-02 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_remove_userprofile_social_delete_socials'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]

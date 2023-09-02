# Generated by Django 4.2.4 on 2023-09-02 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_delete_usersocials'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSocials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
                ('social', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.socialmediatype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.userprofile')),
            ],
        ),
    ]

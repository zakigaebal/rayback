# Generated by Django 4.1.1 on 2022-09-11 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_loginuser_age_loginuser_birth_day_loginuser_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginuser',
            name='email',
            field=models.CharField(default='', max_length=255, verbose_name='이메일 주소'),
        ),
        migrations.AlterField(
            model_name='loginuser',
            name='name',
            field=models.CharField(max_length=20, null=True, verbose_name='이름'),
        ),
    ]

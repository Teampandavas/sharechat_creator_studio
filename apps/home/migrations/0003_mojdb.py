# Generated by Django 3.2.16 on 2022-11-18 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_userdetails_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='MojDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=12)),
                ('post', models.CharField(max_length=50000)),
            ],
        ),
    ]

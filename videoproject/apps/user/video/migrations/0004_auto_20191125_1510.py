# Generated by Django 2.2.5 on 2019-11-25 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0003_auto_20191125_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video_user',
            name='picture',
            field=models.TextField(blank=True, null=True),
        ),
    ]
# Generated by Django 3.2.15 on 2022-09-11 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("forum_polls", "0002_auto_20151105_0029"),
    ]

    operations = [
        migrations.AddField(
            model_name="topicpoll",
            name="hide_results",
            field=models.BooleanField(default=False, verbose_name="Hide results"),
        ),
    ]

# Generated by Django 3.2.5 on 2024-07-25 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dwitter', '0006_auto_20231129_0406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_intro',
            field=models.CharField(blank=True, default='my profile intro', max_length=1000, null=True),
        ),
    ]
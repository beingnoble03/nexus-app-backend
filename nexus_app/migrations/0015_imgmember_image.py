# Generated by Django 4.1.1 on 2022-09-29 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nexus_app', '0014_alter_imgmember_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='imgmember',
            name='image',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]

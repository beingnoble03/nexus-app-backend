# Generated by Django 4.1.1 on 2022-09-23 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nexus_app', '0002_round_round_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imgmember',
            name='branch',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='imgmember',
            name='enrollment_number',
            field=models.IntegerField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='imgmember',
            name='role',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='imgmember',
            name='year',
            field=models.SmallIntegerField(null=True),
        ),
    ]

# Generated by Django 4.1.1 on 2022-10-22 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nexus_app', '0021_alter_panel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interview',
            name='panel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='nexus_app.panel'),
        ),
    ]
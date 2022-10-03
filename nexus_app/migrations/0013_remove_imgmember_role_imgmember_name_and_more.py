# Generated by Django 4.1.1 on 2022-09-29 06:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nexus_app', '0012_alter_applicant_round_alter_applicant_stage_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imgmember',
            name='role',
        ),
        migrations.AddField(
            model_name='imgmember',
            name='name',
            field=models.CharField(default='Noble', max_length=80),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='applicant',
            name='role',
            field=models.CharField(choices=[('dev', 'Developer'), ('des', 'Designer')], max_length=3),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='stage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nexus_app.round'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='status',
            field=models.CharField(choices=[('Evaluated', 'Evaluated'), ('Not Evaluated', 'Not Evaluated'), ('Called', 'Called'), ('Not Called', 'Not Called')], max_length=50, null=True),
        ),
    ]

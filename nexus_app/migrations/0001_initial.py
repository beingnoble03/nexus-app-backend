# Generated by Django 4.1.1 on 2022-09-22 09:37

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImgMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('branch', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=50)),
                ('year', models.SmallIntegerField()),
                ('enrolment_number', models.IntegerField(unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('enrolment_number', models.BigIntegerField(unique=True)),
                ('branch', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=13)),
                ('status', models.CharField(max_length=50)),
                ('stage', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='InterviewSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('maximum_marks', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('maximum_marks', models.IntegerField()),
                ('assignee', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('role', models.CharField(choices=[('dev', 'Developer'), ('des', 'Designer')], max_length=3)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('round', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nexus_app.round')),
            ],
        ),
        migrations.CreateModel(
            name='SectionMarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obtained_marks', models.IntegerField()),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nexus_app.interviewsection')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nexus_app.test')),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obtained_marks', models.IntegerField(verbose_name='Marks')),
                ('remarks', models.CharField(max_length=100)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nexus_app.applicant')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nexus_app.question')),
            ],
        ),
        migrations.AddField(
            model_name='round',
            name='season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rounds', related_query_name='round', to='nexus_app.season'),
        ),
        migrations.AddField(
            model_name='question',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nexus_app.section'),
        ),
        migrations.CreateModel(
            name='Panel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=100)),
                ('available', models.BooleanField()),
                ('status', models.CharField(max_length=50)),
                ('members', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='interviewsection',
            name='round',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nexus_app.round'),
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_assigned', models.DateTimeField(null=True)),
                ('time_entered', models.DateTimeField(null=True)),
                ('completed', models.BooleanField()),
                ('remarks', models.CharField(max_length=100)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nexus_app.applicant')),
                ('panel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nexus_app.panel')),
                ('round', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nexus_app.round')),
                ('section_marks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nexus_app.sectionmarks')),
            ],
        ),
        migrations.AddField(
            model_name='applicant',
            name='round',
            field=models.ManyToManyField(related_name='applicants', related_query_name='applicant', to='nexus_app.round'),
        ),
    ]

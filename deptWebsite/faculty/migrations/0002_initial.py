# Generated by Django 4.0.2 on 2022-03-07 11:31

import django.contrib.sites.managers
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('students', '0001_initial'),
        ('faculty', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scholar',
            fields=[
                ('student_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='students.student')),
                ('research_title', models.CharField(max_length=500)),
                ('research_description', models.TextField()),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phd_scholars', to='faculty.deptperson')),
            ],
            bases=('students.student',),
            managers=[
                ('on_site', django.contrib.sites.managers.CurrentSiteManager('department')),
            ],
        ),
        migrations.AddField(
            model_name='responsibility',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responsiblities', to='faculty.deptperson'),
        ),
        migrations.AddField(
            model_name='researchinterests',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interests', to='faculty.deptperson'),
        ),
        migrations.AddField(
            model_name='publication',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publicaions', to='faculty.deptperson'),
        ),
        migrations.AddField(
            model_name='project',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='faculty.deptperson'),
        ),
        migrations.AddField(
            model_name='patent',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patents', to='faculty.deptperson'),
        ),
        migrations.AddField(
            model_name='event',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='faculty.deptperson'),
        ),
        migrations.AddField(
            model_name='deptperson',
            name='department',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='person', to='sites.site'),
        ),
        migrations.AddField(
            model_name='award',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='awards', to='faculty.deptperson'),
        ),
        migrations.AddField(
            model_name='affilation',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='affilations', to='faculty.deptperson'),
        ),
    ]
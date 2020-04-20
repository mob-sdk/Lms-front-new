# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=255)),
                ('notification', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('seen', models.BooleanField(default=False)),
                ('course_instance', models.ForeignKey(to='course.CourseInstance', on_delete=models.CASCADE)),
                ('recipient', models.ForeignKey(related_name='received_notifications', to='userprofile.UserProfile', on_delete=models.CASCADE)),
                ('sender', models.ForeignKey(related_name='sent_notifications', to='userprofile.UserProfile', on_delete=models.CASCADE)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
            bases=(models.Model,),
        ),
    ]

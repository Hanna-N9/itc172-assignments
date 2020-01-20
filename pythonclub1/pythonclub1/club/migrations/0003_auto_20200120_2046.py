# Generated by Django 3.0.2 on 2020-01-20 20:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('club', '0002_auto_20200114_1809'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventtitle', models.CharField(max_length=255)),
                ('evententrydate', models.DateField()),
                ('eventlocation', models.TextField()),
                ('eventtime', models.TextField()),
                ('eventdescription', models.TextField(blank=True, null=True)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'events',
                'db_table': 'event',
            },
        ),
        migrations.CreateModel(
            name='Meet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meettitle', models.CharField(max_length=255)),
                ('meetentrydate', models.DateField()),
                ('meetlocation', models.TextField()),
                ('meettime', models.TextField()),
                ('meetdescription', models.TextField(blank=True, null=True)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'meets',
                'db_table': 'meet',
            },
        ),
        migrations.CreateModel(
            name='Minute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minutename', models.CharField(max_length=255)),
                ('minutetext', models.TextField()),
                ('User', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('minuteid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='club.Meet')),
            ],
            options={
                'verbose_name_plural': 'minutes',
                'db_table': 'minute',
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resourcename', models.CharField(max_length=255)),
                ('resourceentrydate', models.DateField()),
                ('resourceurl', models.URLField(blank=True, null=True)),
                ('resourcetype', models.TextField()),
                ('User', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'resources',
                'db_table': 'resource',
            },
        ),
        migrations.RenameModel(
            old_name='ProductType',
            new_name='MeetType',
        ),
        migrations.RemoveField(
            model_name='review',
            name='product',
        ),
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
        migrations.AlterModelOptions(
            name='meettype',
            options={'verbose_name_plural': 'MeetTypes'},
        ),
        migrations.AlterModelTable(
            name='meettype',
            table='MeetType',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]

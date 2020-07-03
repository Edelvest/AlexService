# Generated by Django 2.2 on 2020-07-03 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Server name')),
                ('description', models.TextField(verbose_name='Server description')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('server_type', models.CharField(choices=[('VM', 'Virtual'), ('DS', 'Dedicated')], max_length=2, verbose_name='Server type')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='serverlist.Server')),
            ],
        ),
        migrations.CreateModel(
            name='ServerIP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=50, unique=True, verbose_name='ip address')),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='serverlist.Server', verbose_name='Server')),
            ],
        ),
    ]

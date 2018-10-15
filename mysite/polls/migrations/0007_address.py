# Generated by Django 2.1.1 on 2018-10-15 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20181014_1926'),
    ]

    operations = [
        migrations.CreateModel(
            name='address',
            fields=[
                ('address_id', models.AutoField(primary_key=True, serialize=False)),
                ('address_type', models.CharField(max_length=200)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('state', models.CharField(blank=True, max_length=200, null=True)),
                ('zip', models.CharField(blank=True, max_length=200, null=True)),
                ('contact_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Contacts')),
            ],
        ),
    ]
# Generated by Django 2.0.6 on 2018-06-21 06:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=50)),
                ('olusturma_tarihi', models.DateField()),
                ('aciklama', models.TextField(max_length=100)),
                ('alan1', models.CharField(blank=True, max_length=20, null=True)),
                ('alan2', models.CharField(blank=True, max_length=20, null=True)),
                ('alan3', models.CharField(blank=True, max_length=20, null=True)),
                ('alan4', models.CharField(blank=True, max_length=20, null=True)),
                ('alan5', models.CharField(blank=True, max_length=20, null=True)),
                ('alan6', models.CharField(blank=True, max_length=20, null=True)),
                ('alan7', models.CharField(blank=True, max_length=20, null=True)),
                ('alan8', models.CharField(blank=True, max_length=20, null=True)),
                ('auther', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auther_device', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

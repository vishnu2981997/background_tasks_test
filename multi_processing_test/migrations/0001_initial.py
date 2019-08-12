# Generated by Django 2.2.4 on 2019-08-11 14:30

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
            name='ImportRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=1024)),
                ('access_token', models.CharField(max_length=1024)),
                ('queue_url', models.CharField(max_length=1024)),
                ('running', models.BooleanField(default=False, editable=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('started', models.DateTimeField(editable=False)),
                ('ended', models.DateTimeField(editable=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='import_requests', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('url',),
            },
        ),
    ]
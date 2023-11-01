# Generated by Django 4.2.2 on 2023-10-29 15:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('d4e123fe-b0fc-4255-b94f-d7d5c8895819'), primary_key=True, serialize=False)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('time_modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('ratings', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Recipes',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('d4e123fe-b0fc-4255-b94f-d7d5c8895819'), primary_key=True, serialize=False)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('time_modified', models.DateTimeField(auto_now=True)),
                ('text', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('recipes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.recipes')),
            ],
            options={
                'verbose_name_plural': 'Comments',
            },
        ),
    ]
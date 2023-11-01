# Generated by Django 4.2.2 on 2023-11-01 01:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0002_remove_recipes_ratings_alter_comments_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='id',
            field=models.UUIDField(default=uuid.UUID('05ef9255-d642-40ee-a306-dad3679b625f'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ratings',
            name='id',
            field=models.UUIDField(default=uuid.UUID('05ef9255-d642-40ee-a306-dad3679b625f'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='id',
            field=models.UUIDField(default=uuid.UUID('05ef9255-d642-40ee-a306-dad3679b625f'), primary_key=True, serialize=False),
        ),
    ]

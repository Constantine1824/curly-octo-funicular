# Generated by Django 4.2.2 on 2023-11-02 00:12

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0003_alter_comments_id_alter_ratings_id_alter_recipes_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='avg_rating',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='comments',
            name='id',
            field=models.UUIDField(default=uuid.UUID('616dc8d3-3efb-4fc5-85bf-9baf4498bd03'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ratings',
            name='id',
            field=models.UUIDField(default=uuid.UUID('616dc8d3-3efb-4fc5-85bf-9baf4498bd03'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ratings',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='Core.recipes'),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='id',
            field=models.UUIDField(default=uuid.UUID('616dc8d3-3efb-4fc5-85bf-9baf4498bd03'), primary_key=True, serialize=False),
        ),
    ]

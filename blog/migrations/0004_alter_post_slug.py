# Generated by Django 4.2.6 on 2023-10-22 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_alter_post_options_post_published_at_post_slug_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(max_length=256, unique_for_date="published_at"),
        ),
    ]

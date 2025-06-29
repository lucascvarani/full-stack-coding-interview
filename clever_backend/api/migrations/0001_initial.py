# Generated by Django 5.2.3 on 2025-06-24 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('is_favorite', models.BooleanField(default=False)),
                ('image_url', models.URLField()),
                ('photographer', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('hex_color', models.CharField(max_length=7)),
                ('portfolio_url', models.URLField()),
            ],
        ),
    ]

# Generated by Django 4.0.1 on 2022-01-09 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_tag_project_vote_ratio_project_vote_total_review_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_image',
            field=models.ImageField(blank=True, default='default.webp', null=True, upload_to=''),
        ),
    ]
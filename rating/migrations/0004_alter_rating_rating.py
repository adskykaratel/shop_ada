# Generated by Django 5.0.1 on 2024-01-16 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0003_alter_rating_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Too bad'), (4, 'Good'), (2, 'Bad'), (3, 'Normal'), (5, 'Excellent')]),
        ),
    ]

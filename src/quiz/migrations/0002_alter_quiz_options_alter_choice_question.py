# Generated by Django 4.2.7 on 2023-12-04 19:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("quiz", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="quiz",
            options={"verbose_name": "Quiz", "verbose_name_plural": "Quizzes"},
        ),
        migrations.AlterField(
            model_name="choice",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="choices",
                to="quiz.question",
            ),
        ),
    ]

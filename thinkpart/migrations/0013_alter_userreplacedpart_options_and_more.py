# Generated by Django 5.0.3 on 2024-03-21 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thinkpart', '0012_alter_userreplacedpart_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userreplacedpart',
            options={'ordering': ['date']},
        ),
        migrations.AlterField(
            model_name='userreplacedpart',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

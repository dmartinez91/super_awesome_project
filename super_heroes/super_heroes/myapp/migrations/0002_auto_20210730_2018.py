# Generated by Django 3.2.5 on 2021-07-30 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='superheros',
            name='alter_ego',
            field=models.CharField(default='Bob', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='superheros',
            name='catchphrase',
            field=models.CharField(default='Hi', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='superheros',
            name='primary_ability',
            field=models.CharField(default='fly', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='superheros',
            name='secondary_ability',
            field=models.CharField(default='fight', max_length=50),
            preserve_default=False,
        ),
    ]

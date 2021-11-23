# Generated by Django 3.2.9 on 2021-11-23 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detectme', '0004_auto_20211122_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='userentry',
            name='cevap_a',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userentry',
            name='cevap_b',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userentry',
            name='cevap_c',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userentry',
            name='cevap_d',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userentry',
            name='cevap_e',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userentry',
            name='rating',
            field=models.CharField(choices=[('Video', 'Video'), ('test', 'Test')], max_length=15),
        ),
    ]
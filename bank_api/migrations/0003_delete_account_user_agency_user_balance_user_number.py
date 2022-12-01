# Generated by Django 4.1.3 on 2022-12-01 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_api', '0002_account'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Account',
        ),
        migrations.AddField(
            model_name='user',
            name='agency',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='balance',
            field=models.DecimalField(decimal_places=2, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='number',
            field=models.CharField(max_length=9, null=True, unique=True),
        ),
    ]
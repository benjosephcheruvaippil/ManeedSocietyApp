# Generated by Django 4.0.3 on 2022-05-13 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loanapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberdetails',
            name='name',
            field=models.CharField(default='', max_length=301),
        ),
    ]
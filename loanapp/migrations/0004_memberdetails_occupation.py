# Generated by Django 4.0.3 on 2022-06-05 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loanapp', '0003_alter_memberdetails_aadhar_alter_memberdetails_age_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='memberdetails',
            name='occupation',
            field=models.CharField(default='', max_length=300, null=True),
        ),
    ]

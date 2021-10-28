# Generated by Django 3.2.5 on 2021-09-14 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='birthday_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='company',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='end_policy_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='full_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='mail',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone_number',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='policy_num',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='start_policy_date',
            field=models.DateField(null=True),
        ),
    ]
# Generated by Django 4.1 on 2023-06-08 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HUFS', '0002_alter_recommendclass_rec_class_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendclass',
            name='rec_weightmi',
            field=models.FloatField(db_column='rec_weightmi'),
        ),
        migrations.AlterField(
            model_name='recommendclass',
            name='rec_weightpl',
            field=models.FloatField(db_column='rec_weightpl'),
        ),
    ]

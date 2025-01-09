# Generated by Django 4.2.17 on 2025-01-09 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yasviapp', '0015_rename_description_package_details_package_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='campingimage',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=2, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='campingimage',
            name='details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='campingimage',
            name='name',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='campingimage',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='status',
            field=models.BooleanField(choices=[(True, 'Available'), (False, 'Not Available')], default=True),
        ),
    ]

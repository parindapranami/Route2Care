# Generated by Django 3.2.5 on 2021-10-19 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_prescription_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.customer'),
        ),
    ]

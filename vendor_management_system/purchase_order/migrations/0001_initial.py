# Generated by Django 5.0.4 on 2024-05-02 11:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('po_number', models.CharField(max_length=255, unique=True, verbose_name='PO Number')),
                ('order_date', models.DateTimeField(verbose_name='Order Date')),
                ('delivery_date', models.DateTimeField(verbose_name='Delivery Date')),
                ('items', models.JSONField(verbose_name='Items Ordered')),
                ('quantity', models.IntegerField(verbose_name='Total Quantity')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('complete', 'Completed Successfully'), ('cancelled', 'Cancelled')], max_length=255, verbose_name='Status')),
                ('quality_rating', models.FloatField(blank=True, null=True, verbose_name='Quality Rating')),
                ('issue_date', models.DateTimeField(verbose_name='Issue Date')),
                ('acknowledgment_date', models.DateTimeField(blank=True, null=True, verbose_name='Acknowledgment Date')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor.vendor', verbose_name='Vendor')),
            ],
            options={
                'verbose_name': 'Purchase Order',
                'verbose_name_plural': 'Purchase Orders',
            },
        ),
    ]

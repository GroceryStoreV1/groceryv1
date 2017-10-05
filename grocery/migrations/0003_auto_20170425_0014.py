# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 12:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('grocery', '0002_auto_20170417_1935'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('CategoryId', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('CategoryName', models.CharField(max_length=30)),
                ('Description', models.CharField(max_length=30)),
                ('Picture', models.CharField(max_length=30)),
                ('Active', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='customers',
            fields=[
                ('CustomerId', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=30)),
                ('LastName', models.CharField(max_length=30)),
                ('Building', models.CharField(max_length=30)),
                ('Address1', models.CharField(max_length=30)),
                ('Address2', models.CharField(max_length=30)),
                ('City', models.CharField(max_length=30)),
                ('State', models.CharField(max_length=30)),
                ('PostalCode', models.IntegerField()),
                ('Country', models.CharField(max_length=30)),
                ('Phone', models.CharField(max_length=30)),
                ('Email', models.CharField(max_length=30)),
                ('Password', models.CharField(max_length=30)),
                ('CreditCard', models.CharField(max_length=30)),
                ('CreditCardTypeId', models.CharField(max_length=30)),
                ('CardExpMo', models.CharField(max_length=30)),
                ('CardExpYr', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='orderDetails',
            fields=[
                ('OrderDetailID', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('Price', models.CharField(max_length=30)),
                ('Quantity', models.CharField(max_length=30)),
                ('Discount', models.CharField(max_length=30)),
                ('Total', models.CharField(max_length=30)),
                ('Size', models.CharField(max_length=30)),
                ('Color', models.CharField(max_length=30)),
                ('Fulfilled', models.CharField(max_length=30)),
                ('BillDate', models.CharField(max_length=30)),
                ('ShipDate', models.CharField(max_length=30)),
                ('Freight', models.CharField(max_length=30)),
                ('SalesTax', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='orders',
            fields=[
                ('OrderID', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('OrderDate', models.CharField(max_length=30)),
                ('RequiredDate', models.CharField(max_length=30)),
                ('ShipDate', models.CharField(max_length=30)),
                ('Freight', models.CharField(max_length=30)),
                ('SalesTax', models.CharField(max_length=30)),
                ('Timestamp', models.CharField(max_length=30)),
                ('TransactStatus', models.CharField(max_length=30)),
                ('ErrLoc', models.CharField(max_length=30)),
                ('ErrMsg', models.CharField(max_length=30)),
                ('Fulfilled', models.CharField(max_length=30)),
                ('Deleted', models.CharField(max_length=30)),
                ('Paid', models.CharField(max_length=30)),
                ('PaymentDate', models.CharField(max_length=30)),
                ('CustomerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grocery.customers')),
            ],
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('PaymentId', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('PaymentType', models.CharField(max_length=30)),
                ('Allowed', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('ProductID', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('SKU', models.CharField(max_length=30)),
                ('SupplierProductID', models.CharField(max_length=30)),
                ('ProductName', models.CharField(max_length=30)),
                ('ProductDescription', models.CharField(max_length=30)),
                ('QuantityPerUnit', models.CharField(max_length=30)),
                ('UnitSize', models.CharField(max_length=30)),
                ('UnitPrice', models.CharField(max_length=30)),
                ('MSRP', models.CharField(max_length=30)),
                ('AvailableSize', models.CharField(max_length=30)),
                ('AvailableColors', models.CharField(max_length=30)),
                ('SizeID', models.CharField(max_length=30)),
                ('ColorID', models.CharField(max_length=30)),
                ('Discount', models.CharField(max_length=30)),
                ('UnitWeight', models.CharField(max_length=30)),
                ('UnitsInStock', models.CharField(max_length=30)),
                ('UnitsOnOrder', models.CharField(max_length=30)),
                ('ReorderLevel', models.CharField(max_length=30)),
                ('ProductAvailable', models.CharField(max_length=30)),
                ('DiscountAvailable', models.CharField(max_length=30)),
                ('CurrentOrder', models.CharField(max_length=30)),
                ('Picture', models.CharField(max_length=30)),
                ('Ranking', models.CharField(max_length=30)),
                ('Note', models.CharField(max_length=30)),
                ('CategoryID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grocery.category')),
            ],
        ),
        migrations.CreateModel(
            name='shippers',
            fields=[
                ('ShipperID', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('CompanyName', models.CharField(max_length=30)),
                ('Phone', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='suppliers',
            fields=[
                ('SupplierID', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('CompanyName', models.CharField(max_length=30)),
                ('ContactFName', models.CharField(max_length=30)),
                ('ContactLName', models.CharField(max_length=30)),
                ('ContactTitle', models.CharField(max_length=30)),
                ('Address1', models.CharField(max_length=30)),
                ('Address2', models.CharField(max_length=30)),
                ('City', models.CharField(max_length=30)),
                ('State', models.CharField(max_length=30)),
                ('PostalCode', models.IntegerField()),
                ('Country', models.CharField(max_length=30)),
                ('Phone', models.CharField(max_length=30)),
                ('Fax', models.CharField(max_length=30)),
                ('Email', models.CharField(max_length=30)),
                ('WebSite', models.CharField(max_length=30)),
                ('PaymentMethods', models.CharField(max_length=30)),
                ('DiscountType', models.CharField(max_length=30)),
                ('DiscountRate', models.CharField(max_length=30)),
                ('TypeGoods', models.CharField(max_length=30)),
                ('DiscountAvailable', models.CharField(max_length=30)),
                ('CurrentOrder', models.CharField(max_length=30)),
                ('SizeURL', models.CharField(max_length=30)),
                ('Logo', models.CharField(max_length=30)),
                ('Ranking', models.CharField(max_length=30)),
                ('Note', models.CharField(max_length=30)),
                ('CustomerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grocery.customers')),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='SupplierID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grocery.suppliers'),
        ),
        migrations.AddField(
            model_name='orders',
            name='PaymentID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grocery.payment'),
        ),
        migrations.AddField(
            model_name='orders',
            name='ShipperID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grocery.shippers'),
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='OrderID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grocery.orders'),
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='ProductID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grocery.products'),
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='ShipperID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grocery.shippers'),
        ),
    ]
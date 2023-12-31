# Generated by Django 4.2.3 on 2023-07-19 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccInventoy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(max_length=200)),
                ('buyer_name', models.CharField(max_length=200)),
                ('po_style_no', models.CharField(max_length=200)),
                ('receive_qty', models.PositiveIntegerField(default=0)),
                ('sku', models.CharField(blank=True, max_length=200, null=True)),
                ('sewing_finishing', models.CharField(blank=True, max_length=200, null=True)),
                ('receive_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Vendor', models.CharField(blank=True, max_length=225, null=True)),
                ('BuyerName', models.CharField(max_length=225)),
                ('Address', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='DailyProductionLineMenPower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line', models.CharField(max_length=225)),
                ('num_operator', models.PositiveIntegerField(default=0)),
                ('num_helper', models.PositiveIntegerField(default=0)),
                ('date', models.DateField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DailyProductionOuput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line', models.CharField(max_length=255)),
                ('style', models.CharField(max_length=255)),
                ('input_qty', models.PositiveIntegerField(default=0)),
                ('cmp_amount', models.FloatField(default=0.0)),
                ('daily_target', models.PositiveIntegerField(default=0)),
                ('wok_hr', models.PositiveIntegerField(default=10)),
                ('shift_1', models.PositiveIntegerField(default=0)),
                ('shift_2', models.PositiveIntegerField(default=0)),
                ('shift_3', models.PositiveIntegerField(default=0)),
                ('shift_4', models.PositiveIntegerField(default=0)),
                ('shift_5', models.PositiveIntegerField(default=0)),
                ('shift_6', models.PositiveIntegerField(default=0)),
                ('shift_7', models.PositiveIntegerField(default=0)),
                ('shift_8', models.PositiveIntegerField(default=0)),
                ('shift_9', models.PositiveIntegerField(default=0)),
                ('shift_10', models.PositiveIntegerField(default=0)),
                ('shift_11', models.PositiveIntegerField(default=0)),
                ('shift_12', models.PositiveIntegerField(default=0)),
                ('total_output_qty', models.PositiveIntegerField(default=0)),
                ('menpower', models.PositiveIntegerField(default=1)),
                ('cmp_pr_menpower', models.FloatField(default=0.0)),
                ('acc_total_cmp', models.FloatField(default=0.0)),
                ('date', models.DateField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='FabricInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(max_length=200)),
                ('buyer_name', models.CharField(max_length=200)),
                ('po_style_no', models.CharField(max_length=200)),
                ('item_name', models.CharField(blank=True, max_length=200, null=True)),
                ('chall_invoice_no', models.CharField(blank=True, max_length=200, null=True)),
                ('fabric_construction', models.CharField(blank=True, max_length=200, null=True)),
                ('fabric_width', models.CharField(blank=True, max_length=200, null=True)),
                ('fabric_composition', models.CharField(blank=True, max_length=200, null=True)),
                ('color', models.CharField(blank=True, max_length=200, null=True)),
                ('receive_qty', models.PositiveIntegerField(default=0)),
                ('warehouse', models.CharField(max_length=200)),
                ('receive_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderQty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer', models.CharField(max_length=255)),
                ('vendor', models.CharField(blank=True, max_length=255, null=True)),
                ('style', models.CharField(max_length=255)),
                ('item', models.CharField(blank=True, max_length=255, null=True)),
                ('order_qty', models.PositiveIntegerField(default=0)),
                ('cmp', models.FloatField()),
                ('cmp_amount', models.FloatField()),
                ('making_charge', models.PositiveIntegerField(default=0)),
                ('import_export_charge', models.PositiveIntegerField(default=0)),
                ('box_charge', models.PositiveIntegerField(default=0)),
                ('poly_bag', models.PositiveIntegerField(default=0)),
                ('sewing_thread', models.PositiveIntegerField(default=0)),
                ('cmp_condition', models.FloatField()),
                ('date', models.DateField()),
                ('serial_number', models.CharField(max_length=255)),
                ('md_charge', models.CharField(blank=True, max_length=255, null=True)),
                ('delivery', models.DateField(blank=True, null=True)),
                ('fabricETA', models.DateField(blank=True, null=True)),
                ('accETA', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductionInput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line', models.CharField(max_length=255)),
                ('style', models.CharField(max_length=255)),
                ('input_qty', models.PositiveIntegerField(default=0)),
                ('daily_target', models.PositiveIntegerField(default=0)),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductionLine',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ProductionLine', models.CharField(max_length=255)),
                ('daily_target', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Vendor', models.CharField(blank=True, max_length=225, null=True)),
                ('BuyerName', models.CharField(max_length=225)),
                ('StyleCode', models.CharField(max_length=225, unique=True)),
                ('ItemName', models.CharField(blank=True, max_length=225, null=True)),
                ('barcode', models.CharField(blank=True, max_length=225, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WareHouse',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('warehouse_name', models.CharField(max_length=200)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Wh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AccVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=100)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('request_qty', models.IntegerField(default=0)),
                ('request_by', models.CharField(blank=True, max_length=100, null=True)),
                ('request_date', models.DateField(blank=True, null=True)),
                ('request_status', models.CharField(blank=True, max_length=100, null=True)),
                ('remark', models.CharField(blank=True, max_length=100, null=True)),
                ('accinv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.accinventoy')),
            ],
        ),
        migrations.AddField(
            model_name='accinventoy',
            name='warehouse',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.warehouse'),
        ),
        migrations.CreateModel(
            name='AccImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('accinv', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.accinventoy')),
            ],
        ),
    ]

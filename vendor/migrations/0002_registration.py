# Generated by Django 5.0.6 on 2024-05-28 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VAT_TIN', models.CharField(max_length=100)),
                ('CST_TIN', models.CharField(max_length=100)),
                ('C_Excise_Range', models.CharField(max_length=100)),
                ('Commissionerate', models.CharField(max_length=100)),
                ('C_Excise_Reg_No', models.CharField(max_length=100)),
                ('PLA_No', models.CharField(max_length=100)),
                ('Service_Tax_No', models.CharField(max_length=100)),
                ('Import_Export_Code', models.CharField(max_length=100)),
                ('ARN_No', models.CharField(max_length=100)),
                ('Export_House_No', models.CharField(max_length=100)),
                ('Udyog_Aadhar_No', models.CharField(max_length=100)),
                ('Vat_Tin_Date', models.DateField()),
                ('Cst_Tin_Date', models.DateField()),
                ('Subject_To', models.CharField(max_length=100)),
                ('Division', models.CharField(max_length=100)),
                ('GST_No', models.CharField(max_length=100)),
                ('ECC_No', models.CharField(max_length=100)),
                ('PAN_No', models.CharField(max_length=100)),
                ('CIN_NO', models.CharField(max_length=100)),
                ('Import_Export_Date', models.DateField()),
                ('ARN_Date', models.DateField()),
                ('LUT_NO', models.CharField(max_length=100)),
                ('LUT_Date', models.DateField()),
            ],
        ),
    ]
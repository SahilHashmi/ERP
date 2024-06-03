# vendor/admin.py
from django.contrib import admin
from .models import Vendor

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = (
        'company_name',
        'short_name',
        'email_id',
        'contact_no',
        'city',
        'state',
    )
    search_fields = (
        'company_name',
        'short_name',
        'email_id',
        'contact_no',
        'city',
        'state',
    )
    list_filter = ('city', 'state')




# for data2

from django.contrib import admin
from .models import Data2Registration

@admin.register(Data2Registration)
class Data2RegistrationAdmin(admin.ModelAdmin):
    list_display = [
        'VAT_TIN',
        'CST_TIN',
        'C_Excise_Range',
        'Commissionerate',
        'C_Excise_Reg_No',
        'PLA_No',
        'Service_Tax_No',
        'Import_Export_Code',
        'ARN_No',
        'Export_House_No',
        'Udyog_Aadhar_No',
        'Vat_Tin_Date',
        'Cst_Tin_Date',
        'Subject_To',
        'Division',
        'GST_No',
        'ECC_No',
        'PAN_No',
        'CIN_NO',
        'Import_Export_Date',
        'ARN_Date',
        'LUT_NO',
        'LUT_Date',
    ]
    search_fields = [
        'VAT_TIN',
        'CST_TIN',
        'C_Excise_Range',
        'Commissionerate',
        'C_Excise_Reg_No',
        'PLA_No',
        'Service_Tax_No',
        'Import_Export_Code',
        'ARN_No',
        'Export_House_No',
        'Udyog_Aadhar_No',
        'Subject_To',
        'Division',
        'GST_No',
        'ECC_No',
        'PAN_No',
        'CIN_NO',
        'LUT_NO',
    ]
    list_filter = ['Commissionerate', 'Division']
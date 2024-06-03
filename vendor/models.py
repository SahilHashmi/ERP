# vendor/models.py
from django.db import models

# models for Data2

class Vendor(models.Model):
    company_name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=255)
    address = models.TextField()
    website = models.URLField(max_length=255)
    email_id = models.EmailField(max_length=255)
    contact_no = models.CharField(max_length=15)
    footer_message = models.TextField()
    director_name = models.CharField(max_length=255)
    msme_no = models.CharField(max_length=255, blank=True, null=True)
    pin_code = models.CharField(max_length=6)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    district_code = models.CharField(max_length=10)
    state_no_numeric = models.CharField(max_length=10)
    state_code_alpha = models.CharField(max_length=10)

    def __str__(self):
        return self.company_name



# models for Data2

class Data2Registration(models.Model):
    VAT_TIN = models.CharField(max_length=100)
    CST_TIN = models.CharField(max_length=100)
    C_Excise_Range = models.CharField(max_length=100)
    Commissionerate = models.CharField(max_length=100)
    C_Excise_Reg_No = models.CharField(max_length=100)
    PLA_No = models.CharField(max_length=100)
    Service_Tax_No = models.CharField(max_length=100)
    Import_Export_Code = models.CharField(max_length=100)
    ARN_No = models.CharField(max_length=100)
    Export_House_No = models.CharField(max_length=100)
    Udyog_Aadhar_No = models.CharField(max_length=100)
    Vat_Tin_Date = models.DateField()
    Cst_Tin_Date = models.DateField()
    Subject_To = models.CharField(max_length=100)
    Division = models.CharField(max_length=100)
    GST_No = models.CharField(max_length=100)
    ECC_No = models.CharField(max_length=100)
    PAN_No = models.CharField(max_length=100)
    CIN_NO = models.CharField(max_length=100)
    Import_Export_Date = models.DateField()
    ARN_Date = models.DateField()
    LUT_NO = models.CharField(max_length=100)
    LUT_Date = models.DateField()


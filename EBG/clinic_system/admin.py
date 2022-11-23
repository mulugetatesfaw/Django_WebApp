
from django.contrib import admin
from.import models

 #Register your models here.
admin.site.site_header='EBG Clinic Administrator'
admin.site.site_title='EBG clinic System'
admin.site.index_title='Well come to EBG clinic' 

@admin.register(models.Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display=[ 'PatientFname', 'PatientLname']
    search_fields=[' patient_Id', 'PatientFname', 'PatientLname']
    list_filter = [ 'PatientFname', 'PatientLname']


@admin.register(models.Treatment)
class TreatmentAdmin(admin.ModelAdmin):
    list_display = ['TreatmentDate', 'TreatmentName', 'treated_patient']
    search_fields =['TreatmentName','treated_patient']
    list_filter = ['TreatmentDate','TreatmentName']

@admin.register(models.Department) 
class DepartmentAdmin(admin.ModelAdmin):
    list_display =['DepartmentName', 'DeapartmentLocation', 'Deapartment_email']
    search_fields=['DepartmentName', 'DeapartmentLocation', 'Deapartment_email']
    list_filter = ['DepartmentName', 'DeapartmentLocation', 'Deapartment_email']

@admin.register(models.Nurse)
class NurseAdmin(admin.ModelAdmin):
    list_display = ['Nurse_First_Name','Nurse_Last_Name',]
    search_fields = ['Nurse_First_Name','Nurse_Id']
    list_filter = ['Nurse_First_Name','Nurse_Last_Name']


@admin.register(models.medecine)
class medecineAdmin(admin.ModelAdmin):
    list_display = ['RecordDate','Mdedecine_Name','MedecineStatus']
    search_fields = ['Mdedecine_Name']
    list_filter = ['RecordDate','Mdedecine_Name']

@admin.register(models.Clinic)
class ClinicAdmin(admin.ModelAdmin):
    list_display = ['clinicName']
    search_fields = ['clinicName']
    list_filter = ['clinicName'] 
    
 
from django.db import models
from django.db.models.fields.related import ForeignKey


# Create your models here.
class Nurse(models.Model):
        Nurse_Id=models.CharField('Nurse Id',max_length=100)
        Nurse_First_Name= models.CharField('Nurse First Name',max_length=100)
        Nurse_Last_Name=models.CharField('Nurse Last Name',max_length=100)
        Phone_number=models.CharField('Phone No',max_length=100,blank=True) 
        Email =models.EmailField('Email',max_length=100)
        gender=models.CharField('Gender',max_length=100,blank=True)
        def __str__(self):
               return self.Nurse_First_Name 
   
class Patient(models.Model): 
        #Patient history (identification)
        patient_Id =models.CharField('patient id',max_length=100)
        PatientFname =models.CharField('patient First Name',max_length=100)
        nurse=ForeignKey(Nurse,on_delete=models.DO_NOTHING)
        PatientLname =models.CharField('patient Last Name',max_length=100)
        Sex =models.CharField('Sex',max_length=50,blank=True)
        Age =models.IntegerField('Age',blank=True)
        MartialStatus=models.CharField('Martial Status',max_length=100,blank=True)
        Religion =models.CharField('Religion',max_length=300)
        Occupation =models.CharField('Occupation',max_length=300)
        Address =models.CharField('Address',max_length=300)
        History_of_present_illness=models.TextField('History Of Present Illness',blank=True)
        Past_illness=models.TextField('Past Illness',blank=True)
        FamilyHistory=models.TextField('Family History',blank=True)
        Social_And_personal_History=models.TextField('Social And Personal History',blank=True)
        Nutritional_history=models.TextField('Nutritional History',blank=True)
  
        def __str__(self):
                return self.PatientFname +  "      "  +  self.PatientLname            
        
class Clinic(models.Model):
  patient_in_clinic=models.ForeignKey(Patient,on_delete=models.CASCADE)
  clinicName=models.CharField('Clinic Name',max_length=150)
  ClinicAddress=models.CharField('Clinic Address',max_length=200)
  def __str__(self):
          return self.clinicName

class Department(models.Model):
 patient_in_depart=models.ForeignKey(Patient,on_delete=models.CASCADE)
 DepartmentName=models.CharField('Department Name',max_length=100)
 DeapartmentLocation=models.CharField('Department Location',max_length=200)
 Deapartment_email=models.EmailField('Department Email Address',max_length=200)
 def __str__(self):
       return self.DepartmentName

class Treatment(models.Model):
    TreatmentDate= models.DateTimeField('Date Of Treatment',blank=True )
    treated_patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    TreatmentName= models.CharField('Treatment Name',max_length=120)
    treatment_clinic=models.OneToOneField(Clinic,on_delete=models.CASCADE)
    SickLeaveDays=models.DateTimeField('Sick Leave Days',blank=True)
    InvoiceNo =models.IntegerField('Invoice No',blank=True)
    UnitPrice=models.FloatField('Unit Price',blank=True)
    Quantity =models.IntegerField('Quantity',blank=True)
    TotalPrice =models.FloatField('Total Price',blank=True)
    Deliveryprice=models.FloatField('Delivery Price',blank=True)
    InsuredPrice =models.FloatField('Insurance Covered Price',blank=True)
    SelfCoverdPrice=models.FloatField('Self Covered price',blank=True)
    remender=models.FloatField('Remainder',blank=True)

    def __str__(self):
          return self.TreatmentName 
 

class medecine(models.Model):
 RecordDate=models.DateTimeField(' Date Of Record',blank=True)
 patient_who_used=models.ForeignKey(Patient,on_delete=models.CASCADE)
 Mdedecine_Name=models.CharField('Medecine Name',max_length=200)
 MedecineStatus=models.CharField('Medecine Status',max_length=200)

 def __str__(self):
          return self.Mdedecine_Name 
  
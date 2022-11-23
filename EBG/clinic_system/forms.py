from django import forms
from . models import  Nurse,Patient,Clinic,Department,Treatment,medecine

class NurseForm(forms.ModelForm):
    class Meta:
        model =Nurse
        fields = ('__all__') 

class PatientForm(forms.ModelForm):
    class Meta:
        model =Patient
        fields = ('__all__') 
        
class ClinicForm(forms.ModelForm):
    class Meta:
        model =Clinic
        fields = ('__all__')

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ('__all__')
class TreatmentForm(forms.ModelForm):
    class Meta:
        model = Treatment
        fields = ('__all__')        

class medecineForm(forms.ModelForm):
    class Meta:
        model = medecine
        fields = ('__all__')
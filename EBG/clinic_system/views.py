from django.shortcuts import render, redirect
import clinic_system
from . models import Nurse,Patient,Clinic,Department,Treatment,medecine
from . forms import*
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.urls import reverse_lazy
import calendar
from calendar import HTMLCalendar

@login_required(login_url="/login/")
def index(request):
    return render(request, "index.html")

def Nurses(request):
    nurses = Nurse.objects.all()
    return render(request, "clinic_system/nurses.html", {"nurses": nurses})

def Nurse_details(request, id):
    nurse = Nurse.objects.get(pk=id)
    context = {
        "nurse": nurse
    }
    return render(request, "clinic_system/nurse_details.html", context)

def add_Nurse(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = NurseForm()
        else:
            nurse = Nurse.objects.get(pk=id)
            form = NurseForm(instance=nurse)
        return render(request, "clinic_system/add_nurse.html", {"form": form})
    else:
        if id == 0:
            form = NurseForm(request.POST)
        else:
            nurse = Nurse.objects.get(pk=id)
            form = NurseForm(request.POST, instance=nurse)
        if form.is_valid():
            form.save()
        return redirect('nurses')

def patients(request):
    patients = Patient.objects.all()
    context = {
        "patients": patients
    }
    return render(request, "clinic_system/patients.html", context)

def patient_details(request, id):
    patient = Patient.objects.get(pk=id)
    
    return render(request, "clinic_system/patient_details.html",  {"patient": patient})

def add_patient(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = PatientForm()
        else:
            patient = Patient.objects.get(pk=id)
            form = PatientForm(instance=patient)
        return render(request, "clinic_system/add_patient.html", {"form": form})
    else:
        if id == 0:
            form = PatientForm(request.POST)
        else:
            patient = Patient.objects.get(pk=id)
            form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
        return redirect('patients')


def Drugs(request):
    drugs = medecine.objects.all()
    context = {
        "drugs":drugs
    }
    return render(request, "clinic_system/drugs.html", context)

def drug_details(request, id):
    drug = medecine.objects.get(pk=id)
    
    return render(request, "clinic_system/drug_details.html",  {"drug": drug})

def add_drug(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = medecineForm()
        else:
            drug = medecine.objects.get(pk=id)
            form = medecineForm(instance=drug)
        return render(request, "clinic_system/add_drug.html", {"form": form})
    else:
        if id == 0:
            form = medecineForm(request.POST)
        else:
            drug = medecine.objects.get(pk=id)
            form = medecineForm(request.POST, instance=drug)
        if form.is_valid():
            form.save()
        return redirect('drugs')


def Departments(request):
    departments = Department.objects.all()
    return render(request, "clinic_system/departments.html", {"departments":departments})

def add_departments(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = DepartmentForm()
        else:
            department = Department.objects.get(pk=id)
            form = DepartmentForm(instance=department)
        return render(request, "clinic_system/add_department.html", {"form": form})
    else:
        if id == 0:
            form = DepartmentForm(request.POST)
        else:
            department = Department.objects.get(pk=id)
            form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
        return redirect('departments')

def department_details(request, id):
    department = Department.objects.get(pk=id)
    context = {
        "department": department
    }
    return render(request, "clinic_system/department_details.html", context)


    #return render(request, 'treatment_details.html', context)


def Clinics(request):
    clinics = Clinic.objects.all()
    return render(request, "clinic_system/clinics.html", {"clinics": clinics})

def clinic_details(request, id):
    clinic = Clinic.objects.get(pk=id)
    context = {
        "clinic": clinic
    }
    return render(request, "clinic_system/clinic_details.html", context)

def add_clinic(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ClinicForm()
        else:
            clinic =Clinic.objects.get(pk=id)
            form = ClinicForm(instance=clinic)
        return render(request, "clinic_system/add_clinic.html", {"form": form})
    else:
        if id == 0:
            form = ClinicForm(request.POST)
        else:
            clinic = Clinic.objects.get(pk=id)
            form = ClinicForm(request.POST, instance=clinic)
        if form.is_valid():
            form.save()
        return redirect('clinics') 


def Treatments(request):
    treatments= Treatment.objects.all()
    context = {
        "treatments": treatments
    }
    return render(request, "clinic_system/treatments.html", context)

def treatment_details(request, id):
    treatment = Treatment.objects.get(pk=id)
    
    return render(request, "clinic_system/treatment_details.html",  {"treatment": treatment})

def add_treatment(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = TreatmentForm()
        else:
            treatment = Treatment.objects.get(pk=id)
            form = TreatmentForm(instance= treatment)
        return render(request, "clinic_system/add_treatment.html", {"form": form})
    else:
        if id == 0:
            form = TreatmentForm(request.POST)
        else:
            treatment =  Treatment.objects.get(pk=id)
            form = TreatmentForm(request.POST, instance=treatment)
        if form.is_valid():
            form.save()
        return redirect('treatments')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("index")
        else:
            messages.info(request, 'invalid creditials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect("login")

def forgot_pass(request):
    return render(request, 'clinic_system/forgot_password.html')
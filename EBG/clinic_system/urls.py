from django.urls import path
from clinic_system import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #Viewing data
    path("", views.index, name="index"),
    path("patients/", views.patients, name="patients"),
    path("nurses/", views.Nurses, name="nurses"),
    path("departments/", views.Departments, name="departments"),
    path("drugs/", views.Drugs, name="drugs"),
    path("clinics/", views.Clinics, name="clinics"),
    path("treatments/", views.Treatments, name="treatments"),


    #Authentication
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),

   
    #Inserting Data
    path("add_treatment/", views.add_treatment, name="add_treatment"),
    path("add_drug/", views.add_drug, name="add_drug"),
    path("add_patient/", views.add_patient, name="add_patient"),
    path("add_nurse/", views.add_Nurse, name="add_nurse"),
    path("add_department/", views.add_departments, name="add_department"),
    path("add_clinic/", views.add_clinic, name="add_clinic"),
    #Viewing Details
    path("department_details/<int:id>/", views.department_details, name="department_details"),
    path("treatment_details/<int:id>/", views.treatment_details, name="treatment_details"),
    path("patient_details/<int:id>/", views.patient_details, name="patient_details"),
    path("nurse_details/<int:id>/", views.Nurse_details, name="nurse_details"),
    path("drug_details/<int:id>/", views.drug_details, name="drug_details"),
    path("clinic_details/<int:id>/", views.clinic_details, name="clinic_details"),

    #Editing Details
    path("edit_department/<int:id>/", views.add_departments, name="edit_department"),
    path("edit_treatment/<int:id>/", views.add_treatment, name="edit_treatment"),
    path("edit_drug/<int:id>/", views.add_drug, name="edit_drug"),
    path("edit_patient/<int:id>/", views.add_patient, name="edit_patient"),
    path("edit_nurse/<int:id>/", views.add_Nurse, name="edit_nurse"),
    path("edit_clinic/<int:id>/", views.add_clinic, name="edit_clinic"),
    path("forgot_pass/", views.forgot_pass, name="forgot_pass"),
    
    
]
 
from django.shortcuts import render,redirect
import firebase_admin
from firebase_admin import firestore,credentials,storage,auth
import pyrebase
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from datetime import date

db = firestore.client()

# Create your views here.
def MyProfile(request):
    student = db.collection("tbl_studentregister").document(request.session["stid"]).get().to_dict()
    return render(request,"Student/MyProfile.html",{'student':student})
    
def EditProfile(request):
    student_data = db.collection("tbl_studentregister").document(request.session["stid"]).get().to_dict()
    if request.method == "POST":
        StudentName=request.POST.get("txt_name")
        StudentContact=request.POST.get("txt_contact")
        StudentAddress=request.POST.get("txt_address")
        sdata = {"Student_name":StudentName,"Student_contact":StudentContact,"Student_address":StudentAddress}
        db.collection("tbl_studentregister").document(request.session["stid"]).update(sdata)
        return redirect("webstudent:Homepage")
    else:
        return render(request,"Student/EditProfile.html",{"student_data":student_data})

def changepass(request):
    student = db.collection("tbl_studentregister").document(request.session["stid"]).get().to_dict()
    email = student["Student_email"]

    rest_link = firebase_admin.auth.generate_password_reset_link(email)

    send_mail(
        'Reset your password ', #subject
        "\rHello \r\nFollow this link to reset your Project password for your " + email + "\n" + rest_link +".\n If you didn't ask to reset your password, you can ignore this email. \r\n Thanks. \r\n Your D MARKET team.",#body
        settings.EMAIL_HOST_USER,
        [email],
    )
    return redirect("webstudent:Homepage")

def ViewElection(request):
    elect = db.collection("tbl_election").stream()
    elect_data =[]
    for i in elect:
        electdata = i.to_dict()
        edata = {"elect":electdata,"id":i.id}
        elect_data.append(edata)
    return render(request,"Student/ViewElection.html",{"elect":elect_data})

def apply_election(request,id):
    stu = db.collection("tbl_studentregister").document(request.session["stid"]).get().to_dict()
    db.collection("tbl_class_candidate").add({"student_id":request.session["stid"],"election_id":id,"candidate_status":0,"submission_date":str(date.today()),"gender":stu["Student_gender"]})
    return redirect("webstudent:ViewElection")

def Complaint(request):
    complaint = db.collection("tbl_complaint").stream()
    complaint_data =[]
    for i in complaint:
        complaintdata = i.to_dict()
        cdata = {"complaint":complaintdata,"id":i.id}
        complaint_data.append(cdata)
    if request.method=="POST":
        ComplaintTitle=request.POST.get("txt_comptitle")
        ComplaintContent=request.POST.get("txt_compcontent")
        data = {"complaint_title":ComplaintTitle,"complaint_content":ComplaintContent}
        db.collection("tbl_complaint").add(data)
        return render(request,"Student/Complaint.html",{'ComplaintTitle':ComplaintTitle,'ComplaintContent':ComplaintContent})
    else:
        return render(request,"Student/Complaint.html",{"complaint":complaint_data})
def Feedback(request):
    feedback = db.collection("tbl_feedback").stream()
    feedback_data =[]
    for i in feedback:
        feedbackdata = i.to_dict()
        fdata = {"feedback":feedbackdata,"id":i.id}
        feedback_data.append(fdata)
    if request.method=="POST":
        FeedbackContent=request.POST.get("txt_feedback")
        data = {"feedback_content":FeedbackContent}
        db.collection("tbl_feedback").add(data)
        return render(request,"Student/Feedback.html",{'FeedbackContent':FeedbackContent})
    else:
        return render(request,"Student/Feedback.html",{"feedback":feedback_data})
def HomePage(request):
    student = db.collection("tbl_studentregister").document(request.session["stid"]).get().to_dict()
    return render(request,"Student/Homepage.html",{"student":student})


from django.shortcuts import render,redirect
import firebase_admin
from firebase_admin import firestore,credentials,storage,auth
import pyrebase
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

db = firestore.client()

# Create your views here.
def NewStudent(request):
    st=db.collection("tbl_studentregister").where("course_id", "==", request.session["tr_co"]).where("year_id", "==", request.session["tr_yr"]).where("student_status", "==", 0).stream()
    stdnt_data=[]
    for i in st:
        stdata=i.to_dict()
        course = db.collection("tbl_course").document(stdata["course_id"]).get().to_dict()
        dept = db.collection("tbl_department").document(course["department_id"]).get().to_dict()
        year = db.collection("tbl_year").document(stdata["year_id"]).get().to_dict()
        stdntdata={"student":stdata,"id":i.id,"course":course,"department":dept,"year":year}
        stdnt_data.append(stdntdata)
    return render(request,"Teacher/NewStudent.html",{"student":stdnt_data})

def rejected_student(request):
    st=db.collection("tbl_studentregister").where("course_id", "==", request.session["tr_co"]).where("year_id", "==", request.session["tr_yr"]).where("student_status", "==", 2).stream()
    stdnt_data=[]
    for i in st:
        stdata=i.to_dict()
        course = db.collection("tbl_course").document(stdata["course_id"]).get().to_dict()
        dept = db.collection("tbl_department").document(course["department_id"]).get().to_dict()
        year = db.collection("tbl_year").document(stdata["year_id"]).get().to_dict()
        stdntdata={"student":stdata,"id":i.id,"course":course,"department":dept,"year":year}
        stdnt_data.append(stdntdata)
    return render(request,"Teacher/Rejected_students.html",{"student":stdnt_data})

def accepted_student(request):
    st=db.collection("tbl_studentregister").where("course_id", "==", request.session["tr_co"]).where("year_id", "==", request.session["tr_yr"]).where("student_status", "==", 1).stream()
    stdnt_data=[]
    for i in st:
        stdata=i.to_dict()
        course = db.collection("tbl_course").document(stdata["course_id"]).get().to_dict()
        dept = db.collection("tbl_department").document(course["department_id"]).get().to_dict()
        year = db.collection("tbl_year").document(stdata["year_id"]).get().to_dict()
        stdntdata={"student":stdata,"id":i.id,"course":course,"department":dept,"year":year}
        stdnt_data.append(stdntdata)
    return render(request,"Teacher/Accepted_students.html",{"student":stdnt_data})

def Approved_class_candidate(request):##
    candidate = db.collection("tbl_class_candidate").where("candidate_status", "==", 1).stream()
    candidate_data =[]
    for i in candidate:
        candidatedata = i.to_dict()
        election = db.collection("tbl_election").document(candidatedata["election_id"]).get().to_dict()
        student = db.collection("tbl_studentregister").document(candidatedata["student_id"]).get().to_dict()
        cdata = {"candidate":candidatedata,"id":i.id,"election":election,"student":student}
        candidate_data.append(cdata)
    return render(request,"Teacher/Approved_class_candidate.html",{"candidate":candidate_data})
        
def Rejected_class_candidate(request):
    candidate = db.collection("tbl_election").stream()
    candidate_data =[]
    for i in candidate:
        candidatedata = i.to_dict()
        cdata={"candidate":candidatedata,"id":i.id}
        candidate_data.append(cdata)
    return render(request,"Teacher/Rejected_class_candidate.html",{"candidatedata":candidate_data})
        
def college_candidate(request):
    candidate = db.collection("tbl_college_candidate").stream()
    candidate_data =[]
    for i in candidate:
        candidatedata = i.to_dict()
        election = db.collection("tbl_election").document(candidatedata["election_id"]).get().to_dict()
        student = db.collection("tbl_studentregister").document(candidatedata["student_id"]).get().to_dict()
        cdata = {"candidate":candidatedata,"id":i.id,"election":election,"student":student}
        candidate_data.append(cdata)
    return render(request,"Teacher/View_college_candidate.html",{"candidate":candidate_data})
        
def Verified_college_candidate(request):
    candidate = db.collection("tbl_election").stream()
    candidate_data =[]
    for i in candidate:
        candidatedata = i.to_dict()
        cdata={"candidate":candidatedata,"id":i.id}
        candidate_data.append(cdata)
    return render(request,"Teacher/Verified_college_candidate.html",{"candidatedata":candidate_data})

def Rejected_college_candidate(request):
    candidate = db.collection("tbl_election").stream()
    candidate_data =[]
    for i in candidate:
        candidatedata = i.to_dict()
        cdata={"candidate":candidatedata,"id":i.id}
        candidate_data.append(cdata)
    return render(request,"Teacher/Rejected_college_candidate.html",{"candidatedata":candidate_data})

def accept_student(request,id):
    student =db.collection("tbl_studentregister").document(id).get().to_dict()
    data =  {"student_status":1} 
    db.collection("tbl_studentregister").document(id).update(data)
    return redirect("webteacher:Homepage")  
def College_Polling(request):
    polling = db.collection("tbl_college_polling").stream()
    polling_data =[]
    for i in polling:
        pollingdata = i.to_dict()
        pdata={"polling":pollingdata,"id":i.id}
        polling_data.append(pdata)
    return render(request,"teacher/View_Collegepolling.html",{"pollingdata":polling_data})
def Class_Polling(request):
    polling = db.collection("tbl_class_polling").stream()
    polling_data =[]
    for i in polling:
        pollingdata = i.to_dict()
        pdata={"polling":pollingdata,"id":i.id}
        polling_data.append(pdata)
    return render(request,"teacher/View_Classpolling.html",{"pollingdata":polling_data})
def class_candidate(request):
    candidate = db.collection("tbl_class_candidate").where("candidate_status", "==", 0).stream()
    candidate_data =[]
    for i in candidate:
        candidatedata = i.to_dict()
        election = db.collection("tbl_election").document(candidatedata["election_id"]).get().to_dict()
        student = db.collection("tbl_studentregister").document(candidatedata["student_id"]).get().to_dict()
        cdata = {"candidate":candidatedata,"id":i.id,"election":election,"student":student}
        candidate_data.append(cdata)
    return render(request,"Teacher/ViewClasscandidate.html",{"candidate":candidate_data})

def reject_student(request,id):
    student =db.collection("tbl_studentregister").document(id).get().to_dict()
    data =  {"student_status":2} 
    db.collection("tbl_studentregister").document(id).update(data)
    return redirect("webteacher:Homepage")

def MyProfile(request):
    teacher = db.collection("tbl_teacher").document(request.session["tr_id"]).get().to_dict()
    return render(request,"Teacher/MyProfile.html",{'teacher':teacher})

def EditProfile(request):
    teacher_data = db.collection("tbl_teacher").document(request.session["tr_id"]).get().to_dict()
    if request.method == "POST":
        TeacherName=request.POST.get("txt_name")
        TeacherContact=request.POST.get("txt_contact")
        TeacherAddress=request.POST.get("txt_address")
        tdata = {"teacher_name":TeacherName,"teacher_contact":TeacherContact,"teacher_address":TeacherAddress}
        db.collection("tbl_teacher").document(request.session["tr_id"]).update(tdata)
        return redirect("webteacher:Homepage")
    else:
        return render(request,"Teacher/EditProfile.html",{"teacher_data":teacher_data})

def changepass(request):
    teacher = db.collection("tbl_teacher").document(request.session["tr_id"]).get().to_dict()
    email = teacher["teacher_email"]

    reset_link = firebase_admin.auth.generate_password_reset_link(email)

    send_mail(
        'Reset your password ', #subject
        "\rHello \r\nFollow this link to reset your Project password for your " + email + "\n" + reset_link +".\n If you didn't ask to reset your password, you can ignore this email. \r\n Thanks. \r\n Your D MARKET team.",#body
        settings.EMAIL_HOST_USER,
        [email],
    )
    return redirect("webstudent:Homepage")

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
        return render(request,"Teacher/Complaint.html",{'ComplaintTitle':ComplaintTitle,'ComplaintContent':ComplaintContent})
    else:
        return render(request,"Teacher/Complaint.html",{"complaint":complaint_data})
def View_Reply(request):
    reply = db.collection("tbl_complaint").stream()
    reply_data =[]
    for i in reply:
        replydata = i.to_dict()
        rdata={"reply":replydata,"id":i.id}
        reply_data.append(rdata)
    return render(request,"Teacher/View_Reply.html",{"replydata":reply_data})
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
        return render(request,"Teacher/Feedback.html",{'FeedbackContent':FeedbackContent})
    else:
        return render(request,"Teacher/Feedback.html",{"feedback":feedback_data})
        
def HomePage(request):
    return render(request,"Teacher/Homepage.html")

def accept_class_candidate(request,id):
    class_can = db.collection("tbl_class_candidate").document(id).update({"candidate_status":1})
    return redirect("webteacher:ViewClasscandidate")

def reject_class_candidate(request,id):
    class_can = db.collection("tbl_class_candidate").document(id).update({"candidate_status":2})
    return redirect("webteacher:ViewClasscandidate")

def verifivote(request):
    student = db.collection("tbl_studentregister").where("course_id", "==", request.session["tr_co"]).where("year_id", "==", request.session["tr_yr"]).stream()
    vote_data = []
    for s in student:
        vote = db.collection("tbl_classpolling").where("student_id", "==", s.id).where("polling_status", "==", 0).stream()
        for v in vote:
            vote_data.append({"studentvote":v.to_dict(),"id":v.id,"student":s.to_dict()})
    return render(request,"Teacher/Verifi_votes.html",{"vote":vote_data})

def verifing(request,id):
    db.collection("tbl_classpolling").document(id).update({"polling_status":1})
    return redirect("webteacher:verifivote")
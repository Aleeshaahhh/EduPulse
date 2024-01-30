from django.shortcuts import render,redirect
import firebase_admin
from firebase_admin import firestore,credentials,storage,auth
import pyrebase
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from datetime import date,datetime
from django.utils import timezone
from operator import itemgetter

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
    electioncount = db.collection("tbl_class_candidate").where("student_id", "==", request.session["stid"]).stream()
    flage = 0
    for ec in electioncount:
        flage = flage + 1
    elect = db.collection("tbl_election").stream()
    elect_data =[]
    for i in elect:
        electdata = i.to_dict()
        edata = {"elect":electdata,"id":i.id}
        elect_data.append(edata)
    return render(request,"Student/ViewElection.html",{"elect":elect_data,"flage":flage})

def apply_election(request,id):
    stu = db.collection("tbl_studentregister").document(request.session["stid"]).get().to_dict()
    db.collection("tbl_class_candidate").add({"student_id":request.session["stid"],"election_id":id,"candidate_status":0,"submission_date":str(date.today()),"gender":stu["Student_gender"],"winner":false})
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
    ele = db.collection("tbl_election").stream()
    ele_data = []
    for e in ele:
        eledata = e.to_dict()
        status = eledata["election_status"]
    # formatted_date = datetime.strptime(datedata, '%Y-%m-%d').date()
    # day_of_month = formatted_date.day
    # # print(day_of_month)
    # today_date = date.today()
    # # print(today_date.day)
    # flage = 0
    # if day_of_month == today_date.day:
    #     flage = 1
    # current_time = timezone.now()
    # # print(current_time.hour)
    poll = db.collection("tbl_classpolling").where("student_id", "==", request.session["stid"]).stream()
    flag = 0
    poll_data = []
    for p in poll:
        flag = flag + 1
    student = db.collection("tbl_studentregister").document(request.session["stid"]).get().to_dict()
    winner = db.collection("tbl_class_candidate").where("winner", "==", True).stream()
    win = []
    for w in winner:
        winn = w.to_dict()
        student = db.collection("tbl_studentregister").document(winn["student_id"]).get().to_dict()
        win.append({"winner":student})
    return render(request,"Student/Homepage.html",{"student":student,"status":status,"flag":flag,"winner":win})

def view_candidate(request, id):
    student = db.collection("tbl_studentregister").document(request.session["stid"]).get().to_dict()
    courseid = student["course_id"]
    yearid = student["year_id"]
    std = db.collection("tbl_studentregister").where("course_id", "==", courseid).where("year_id", "==", yearid).stream()
    std_data = []

    for st in std:
        candidate = db.collection("tbl_class_candidate").where("student_id", "==", st.id).where("candidate_status", ">=", 2).stream()
        for can in candidate:
            c = can.to_dict()
            polling = db.collection("tbl_classpolling").where("candidate_id", "==", can.id).stream()
            vote_count = len(list(polling))
            std_data.append({"candidate": can.to_dict(), "id": can.id, "student": st.to_dict(), "count": vote_count})

    # Find the candidate with the highest vote count
    winner = max(std_data, key=itemgetter('count'))

    # Update the winner field in the database
    winning_candidate_id = winner["id"]
    db.collection("tbl_class_candidate").document(winning_candidate_id).update({"winner": True})

    return render(request, "Student/View_class_candidate.html", {"std": std_data})

def addclasspolling(request):
    student = db.collection("tbl_studentregister").document(request.session["stid"]).get().to_dict()
    courseid = student["course_id"]
    yearid = student["year_id"]
    std = db.collection("tbl_studentregister").where("course_id", "==", courseid).where("year_id", "==", yearid).stream()
    std_data = []
    for st in std:
        candidate = db.collection("tbl_class_candidate").where("student_id", "==", st.id).stream()
        for can in candidate:
            c = can.to_dict()
            std_data.append({"candidate":can.to_dict(),"id":can.id,"student":st.to_dict()})
    return render(request,"Student/AddPolling.html",{"std":std_data})

def vote(request,id):
    # candi = db.collection("tbl_class_candidate").document(id).get().to_dict()
    db.collection("tbl_classpolling").add({"student_id":request.session["stid"],"candidate_id":id,"datetime":timezone.now(),"polling_status":0})
    return render(request,"Student/Homepage.html",{"msg":"Polling Added"})

def viewresult(request):
    # student = db.collection("tbl_studentregister").document(request.session["stid"]).get().to_dict()
    # year = student["year_id"]
    # course = student["course_id"]
    # myclass = db.collection("tbl_studentregister").where("year_id", "==", year).where("course_id", "==", course).stream()
    # std_ids = []
    # for mc in myclass:
    #     std_ids.append(mc.id)
    # # print(std_ids)
    # candi = db.collection("tbl_classpolling").stream()
    # can_ids = []
    # for c in candi:
    #     ca = c.to_dict()
    #     can_ids.append(ca["candidate_id"])
    # # print(can_ids)
    # final_id = set()
    # for stid in std_ids:
    #     for canid in can_ids:
    #         if stid == canid:
    #             final_id.add(stid)
    # # print(list(final_id))
    # fids = list(final_id)
    # candidate = db.collection("tbl_classpolling").where("candidate_id", "==", fids).where("polling_status", "==", 1).stream()
    # can_final = []
    # for ca in candidate:
    #     candi = ca.to_dict()
    #     student = db.collection("tbl_studentregister").document(candi["candidate_id"]).get().to_dict()
    #     can_final.append({"student":student})
    # print(can_final)

    student = db.collection("tbl_studentregister").document(request.session["stid"]).get().to_dict()
    year = student["year_id"]
    course = student["course_id"]
    candidate  = db.collection("tbl_class_candidate").where("student_id.course_id", "==", course).where("student_id.year_id", "==", year).stream()
    for c in candidate:
        can = c.to_dict()
        print(can)
        student = db.collection("tbl_studentregister").document(can["candidate_id"])

    return render(request,"Student/View_result.html")
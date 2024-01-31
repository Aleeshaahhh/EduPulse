from django.shortcuts import render,redirect
import firebase_admin
from firebase_admin import firestore,credentials,storage,auth
import pyrebase
from datetime import date

db = firestore.client()

config = {
  "apiKey": "AIzaSyAGFtJubfPzJ_Yxp_lReF3RLI4HWp9XU0Y",
  "authDomain": "edupulse-e5cc1.firebaseapp.com",
  "projectId": "edupulse-e5cc1",
  "storageBucket": "edupulse-e5cc1.appspot.com",
  "messagingSenderId": "146049395522",
  "appId": "1:146049395522:web:7661858773de3b56d436db",
  "measurementId": "G-V7P675TP0Q",
  "databaseURL": ""
}

firebase = pyrebase.initialize_app(config)
st = firebase.storage()
authe = firebase.auth()

# Create your views here.
def Department(request):
    dep = db.collection("tbl_department").stream()
    dep_data = []
    for i in dep:
        depdata = i.to_dict()
        ddata = {"dept":depdata,"id":i.id}
        dep_data.append(ddata)
        # dep_data.append({"dept":i.to_dict(),"id":i.id})
    if request.method=="POST":
        Department=request.POST.get("txt_department")
        data = {"department_name":Department}
        db.collection("tbl_department").add(data)
        return render(request,"Admin/Department.html",{'Department':Department})
    else:
        return render(request,"Admin/Department.html",{"depdata":dep_data})

def delete_dept(request,id):
    db.collection("tbl_department").document(id).delete()
    return redirect("webadmin:Department")

def edit_dept(request,id):
    dept = db.collection("tbl_department").document(id).get().to_dict()
    if request.method == "POST":
        Department=request.POST.get("txt_department")
        data = {"department_name":Department}
        db.collection("tbl_department").document(id).update(data)
        return redirect("webadmin:Department")
    else:
        return render(request,"Admin/Department.html",{"dept":dept})

def Year(request):
    yr=db.collection("tbl_year").stream()
    yr_data=[]
    for i in yr:
        yrdata=i.to_dict()
        ydata={"year":yrdata,"id":i.id}
        yr_data.append(ydata)
    if request.method=="POST":
        Year=request.POST.get("txt_year")
        data = {"year_name":Year}
        db.collection("tbl_year").add(data)
        return render(request,"Admin/Year.html",{'Year':Year})
    else:
        return render(request,"Admin/Year.html",{"yrdata":yr_data})

def Admin_registration(request):
    if request.method=="POST":
        Name=request.POST.get("txt_name")
        Email=request.POST.get("txt_email")
        Password=request.POST.get("txt_password")

        try:
            admin = firebase_admin.auth.create_user(email=Email,password=Password)
        except (firebase_admin._auth_utils.EmailAlreadyExistsError,ValueError) as error:
            return render(request,"Admin/Admin_registration.html",{"msg":error})
        db.collection("tbl_admin").add({"admin_name":Name,"admin_email":Email,"admin_id":admin.uid})
        return render(request,"Admin/Admin_registration.html",{"msg":"Account Created.."})
    else:
        return render(request,"Admin/Admin_registration.html")
def Course(request):
    dep = db.collection("tbl_department").stream()
    dep_data = []
    for i in dep:
        dep_data.append({"dept":i.to_dict(),"id":i.id})
    course=db.collection("tbl_course").stream()
    course_data=[]
    for i in course:
        course_list=i.to_dict()
        dept=course_list["department_id"]
        depart=db.collection("tbl_department").document(dept).get()
        Department=depart.to_dict()
        # print(Department)
        course_data.append({"course":course_list,"id":i.id,"depart_data":Department})
    if request.method=="POST":
        Department=request.POST.get("dept")
        Course=request.POST.get("txt_course")
        data = {"course_name":Course,"department_id":Department}
        db.collection("tbl_course").add(data)
        # db.collection("tbl_course").add({"course_name":request.POST.get("txt_course"),"department_id":request.POST.get("dept")})
        return render(request,"Admin/Course.html",{'Department':Department,'Course':Course})
    else:
        return render(request,"Admin/Course.html",{"dept":dep_data,"course":course_data})

def delete_course(request,id):
    db.collection("tbl_course").document(id).delete()
    return redirect("webadmin:Course")

def edit_course(request,id):
    dep = db.collection("tbl_department").stream()
    dep_data = []
    for i in dep:
        dep_data.append({"dept":i.to_dict(),"id":i.id})
    course = db.collection("tbl_course").document(id).get().to_dict()
    if request.method == "POST":
        Department=request.POST.get("dept")
        Course=request.POST.get("txt_course")
        data = {"course_name":Course,"department_id":Department}
        db.collection("tbl_course").document(id).update(data)
        return redirect("webadmin:Course")
    else:
        return render(request,"Admin/Course.html",{"coursedata":course,"dept":dep_data})

def Election(request):
    elect = db.collection("tbl_election").stream()
    elect_data =[]
    for i in elect:
        electdata = i.to_dict()
        edata = {"elect":electdata,"id":i.id}
        elect_data.append(edata)
    if request.method=="POST":
        ElectionDate=request.POST.get("txt_electdate")
        ElectionDetails=request.POST.get("txt_electdetails")
        data = {"election_for_date":ElectionDate,"election_details":ElectionDetails,"election_date":str(date.today()),"election_nomination_ldate":request.POST.get("txt_nldate"),"election_nomination_cdate":request.POST.get("txt_ncdate"),"election_status":0}
        db.collection("tbl_election").add(data)
        return render(request,"Admin/Election.html",{'ElectionDate':ElectionDate,'ElectionDetails':ElectionDetails})
    else:
        return render(request,"Admin/Election.html",{"elect":elect_data})

def delete_election(request,id):
    db.collection("tbl_election").document(id).delete()
    return redirect("webadmin:Election")

def edit_election(request,id):
    db.collection("tbl_election").document(id).update({"election_status":1})
    return redirect("webadmin:Election")

def deactive(request,id):
    db.collection("tbl_election").document(id).update({"election_status":0})
    return redirect("webadmin:Election")

def Teacher(request):
    tr=db.collection("tbl_teacher").stream()
    tchr_data=[]
    for i in tr:
        trdata=i.to_dict()
        course = db.collection("tbl_course").document(trdata["course_id"]).get().to_dict()
        dept = db.collection("tbl_department").document(course["department_id"]).get().to_dict()
        year = db.collection("tbl_year").document(trdata["year_id"]).get().to_dict()

        tcrdata={"teacher":trdata,"id":i.id,"course":course,"department":dept,"year":year}
        tchr_data.append(tcrdata)
    dep = db.collection("tbl_department").stream()
    dep_data = []
    for i in dep:
        depdata = i.to_dict()
        ddata = {"dept":depdata,"id":i.id}
        dep_data.append(ddata)
    yr=db.collection("tbl_year").stream()
    yr_data=[]
    for i in yr:
        yrdata=i.to_dict()
        ydata={"year":yrdata,"id":i.id}
        yr_data.append(ydata)
    
    if request.method=="POST":
        Email=request.POST.get("txt_email")
        Password=request.POST.get("txt_password")
        try:
            teacher = firebase_admin.auth.create_user(email=Email,password=Password)
        except (firebase_admin._auth_utils.EmailAlreadyExistsError,ValueError) as error:
            return render(request,"Admin/Teacher.html",{"msg":error})
        Photo=request.FILES.get("txt_photo")
        if Photo:
            path = "Teacher_Photo/" + Photo.name
            st.child(path).put(Photo)
            d_url = st.child(path).get_url(None)
        data = {"teacher_id":teacher.uid,"teacher_name":request.POST.get("txt_name"),"teacher_email":Email,"teacher_contact":request.POST.get("txt_contact"),"teacher_photo":d_url,"course_id":request.POST.get("sel_course"),"year_id":request.POST.get("year"),"teacher_address":request.POST.get("txtaddress")}
        db.collection("tbl_teacher").add(data)
        return render(request,"Admin/Teacher.html",{"msg":"Account Created.."})
    else:
        return render(request,"Admin/Teacher.html",{"depdata":dep_data,"yrdata":yr_data,"tchrdata":tchr_data})

def ajaxteacher(request):
    msg = ""
    if (request.GET.get("cid") !="") and (request.GET.get("yid") !=""):
        teacher = db.collection("tbl_teacher").where("course_id", "==", request.GET.get("cid")).where("year_id", "==", request.GET.get("yid")).stream()
        flag = 0
        for t in teacher:
            flag = flag + 1
        if flag > 0:
            msg = "Teacher Already Assign"
        return render(request,"Admin/AjaxTeacher.html",{"msg":msg})
    else:
        return render(request,"Admin/AjaxTeacher.html",{"msg":msg})

def delete_student(request,id):
    db.collection("tbl_teacher").document(id).delete()
    return redirect("webadmin:Teacher")
def Assign_ElectionTeacher(request):
    assign = db.collection("tbl_teacher").stream()
    assign_data=[]
    for i in assign:
        assigndata=i.to_dict()
        adata={"assign":assigndata,"id":i.id}
        assign_data.append(adata)
    if request.method=="POST":
        Date=request.POST.get("txt_date")
        Election_Details=request.POST.get("txt_electiondetails")
        Teacher=request.POST.get("txt_teacher")
        data = {"date":Date,"election_deatils":Election_Details,"Teacher":Teacher}
        db.collection("tbl_assign_teacher").add(data)
        return render(request,"Admin/Assign_ElectionTeacher.html",{"assign":Teacher})
    else:
        return render(request,"Admin/Assign_ElectionTeacher.html",{"teacher_name":assign_data})

def Assigned_Teacher(request):
    teacher = db.collection("tbl_assign_teacher").stream()
    teacher_data =[]
    for i in teacher:
        teacherdata = i.to_dict()
        tdata={"teacher":teacherdata,"id":i.id}
        teacher_data.append(tdata)
    return render(request,"Admin/View_AssignedTeacher.html",{"teacherdata":teacher_data})
def RepliedStudentComplaint(request):
    reply = db.collection("tbl_complaint").stream()
    reply_data =[]
    for i in reply:
        replydata = i.to_dict()
        rdata={"reply":replydata,"id":i.id}
        reply_data.append(rdata)
    return render(request,"Admin/View_RepliedStudentComplaint.html",{"replydata":reply_data})
def RepliedTeacherComplaint(request):
    reply = db.collection("tbl_complaint").stream()
    reply_data =[]
    for i in reply:
        replydata = i.to_dict()
        rdata={"reply":replydata,"id":i.id}
        reply_data.append(rdata)
    return render(request,"Admin/View_RepliedTeacherComplaint.html",{"replydata":reply_data})

def Classelection_Result(request):
    candidate = db.collection("tbl_class_candidate").where("candidate_status", ">=", 1).stream()
    can_data = []
    for c in candidate:
        pocount = 0
        can = c.to_dict()
        student = db.collection("tbl_studentregister").document(can["student_id"]).get().to_dict()
        year = db.collection("tbl_year").document(student["year_id"]).get().to_dict()
        course = db.collection("tbl_course").document(student["course_id"]).get().to_dict()
        polling = db.collection("tbl_classpolling").where("candidate_id", "==",c.id).where("polling_status", "==", 1).stream()
        for po in polling:
            pocount = pocount + 1
        can_data.append({"candidate":c.to_dict(),"id":c.id,"student":student,"count":pocount,"year":year,"course":course})
    return render(request,"Admin/View_Classelection_Result.html",{"candidate":can_data})

def publish_classres(request):
    can = db.collection("tbl_class_candidate").where("candidate_status", "==", 1).stream()
    for c in can:
        db.collection("tbl_class_candidate").document(c.id).update({"candidate_status":2})
    return redirect("webadmin:View_Classelection_Result")

def Collegeelection_Result(request):
    result = db.collection("tbl_college_polling").stream()
    result_data =[]
    for i in result:
        resultdata = i.to_dict()
        rdata={"result":resultdata,"id":i.id}
        result_data.append(rdata)
    return render(request,"Admin/View_Collegeelection_Result.html",{"resultdata":result_data})
def Teacher_Complaint(request):
    complaint = db.collection("tbl_complaint").stream()
    complaint_data =[]
    for i in complaint:
        complaintdata = i.to_dict()
        cdata={"complaint":complaintdata,"id":i.id}
        complaint_data.append(cdata)
    return render(request,"Admin/ViewTeacher_Complaint.html",{"complaintdata":complaint_data})
def Student_Complaint(request):
    complaint = db.collection("tbl_complaint").stream()
    complaint_data =[]
    for i in complaint:
        complaintdata = i.to_dict()
        cdata={"complaint":complaintdata,"id":i.id}
        complaint_data.append(cdata)
    return render(request,"Admin/ViewStudent_Complaint.html",{"complaintdata":complaint_data})
def ComplaintReply(request):
    reply = db.collection("tbl_complaint").stream()
    reply_data=[]
    for i in reply:
        replydata=i.to_dict()
        rdata={"reply":replydata,"id":i.id}
        reply_data.append(rdata)
    if request.method=="POST":
        Reply=request.POST.get("txt_reply")
        data = {"reply":Reply}
        db.collection("tbl_complaint_reply").add(data)
        return render(request,"Admin/ComplaintReply.html",{"reply":Reply})
    else:
        return render(request,"Admin/ComplaintReply.html",{"reply":reply_data})

def ajaxcourse(request):
    course = db.collection("tbl_course").where("department_id", "==", request.GET.get("depid")).stream()
    course_data = []
    for i in course:
        course_data.append({"course":i.to_dict(),"id":i.id})
    return render(request,"Admin/AjaxCourse.html",{"course":course_data})      
def HomePage(request):
    return render(request,"Admin/Homepage.html")  

def logout(request):
    del request.session["aid"]
    return redirect("webguest:Login")
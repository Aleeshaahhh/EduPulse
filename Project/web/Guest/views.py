from django.shortcuts import render,redirect
import firebase_admin
from firebase_admin import firestore,credentials,storage,auth
import pyrebase


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
def Login(request):
    st_id = "" 
    tr_id = teacher_course = ""
    if request.method=="POST":
        Email=request.POST.get("txt_email")
        Password=request.POST.get("txt_password")

        try:
            data = authe.sign_in_with_email_and_password(Email,Password)
        except:
            return render(request,"Guest/Login.html",{"msg":"Error In Email Or Password.."})
        data_id = data["localId"]
        student = db.collection("tbl_studentregister").where("Student_id", "==", data_id).where("student_status", "==", 1).stream()
        for s in student:
            st_id = s.id
        teacher = db.collection("tbl_teacher").where("teacher_id", "==", data_id).stream()
        for t in teacher:
            tr_id= t.id
            teacher_data = t.to_dict()
            teacher_course = teacher_data["course_id"]
        if st_id:
            request.session["stid"] = st_id
            return redirect("webstudent:Homepage")
        elif tr_id:
            request.session["tr_id"]=tr_id
            request.session["tr_co"] = teacher_course
            return redirect("webteacher:Homepage")
        else:
            return render(request,"Guest/Login.html",{"msg":"Error"})
    else:
        return render(request,"Guest/Login.html")
def Student_Register(request):
    dep = db.collection("tbl_department").stream()
    dep_data = []
    for i in dep:
        depdata = i.to_dict()
        ddata = {"dept":depdata,"id":i.id}
        dep_data.append(ddata)
        # dep_data.append({"dept":i.to_dict(),"id":i.id})
    yr=db.collection("tbl_year").stream()
    yr_data=[]
    for i in yr:
        yrdata=i.to_dict()
        ydata={"year":yrdata,"id":i.id}
        yr_data.append(ydata)
    if request.method=="POST":
        Email=request.POST.get("txt_email")
        Password=request.POST.get("txt_password")
        Proof=request.FILES.get("txt_proof")

        try:
            Student_Register = firebase_admin.auth.create_user(email=Email,password=Password)
        except (firebase_admin._auth_utils.EmailAlreadyExistsError,ValueError) as error:
            return render(request,"Guest/Student_Register.html",{"msg":error})

        if Proof:
            path = "Student_proof/" + Proof.name
            st.child(path).put(Proof)
            dwnld_url = st.child(path).get_url(None)
        Photo=request.FILES.get("txt_photo")
        if Photo:
            path = "Student_Photo/" + Photo.name
            st.child(path).put(Photo)
            d_url = st.child(path).get_url(None)
        data = {"Student_id":Student_Register.uid,"Student_name":request.POST.get("txt_name"),"Student_email":Email,"Student_contact":request.POST.get("txt_contact"),"Student_proof":dwnld_url,"Student_photo":d_url,"course_id":request.POST.get("sel_course"),"year_id":request.POST.get("year"),"Student_address":request.POST.get("txt_address"),"Student_admissionno":request.POST.get("txt_admino"),"Student_gender":request.POST.get("txt_gender"),"student_status":0}
        db.collection("tbl_studentregister").add(data)
        return render(request,"Guest/Student_Register.html",{"msg":"Account Created.."})
    else:
        return render(request,"Guest/Student_Register.html",{"department":dep_data,"year":yr_data})
def index(request):
     return render(request,"Guest/index.html")

def ajaxcourse(request):
    course = db.collection("tbl_course").where("department_id", "==", request.GET.get("depid")).stream()
    course_data = []
    for i in course:
        course_data.append({"course":i.to_dict(),"id":i.id})
    return render(request,"Guest/AjaxCourse.html",{"course":course_data})
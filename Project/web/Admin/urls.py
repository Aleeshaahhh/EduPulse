from django.urls import path,include
from Admin import views

app_name="webadmin"

urlpatterns = [
     path('Department/',views.Department,name="Department"),
     path('delete_dept/<str:id>',views.delete_dept,name="delete_dept"),
     path('edit_dept/<str:id>',views.edit_dept,name="edit_dept"),
    path('Year/',views.Year),
    path('Admin_registration/',views.Admin_registration),
    path('Course/',views.Course,name="Course"),
     path('delete_course/<str:id>',views.delete_course,name="delete_course"),
     path('edit_course/<str:id>',views.edit_course,name="edit_course"),
    path('Department/',views.Department),
    path('Election/',views.Election,name="Election"),
    path('delete_election/<str:id>',views.delete_election,name="delete_election"),
     path('edit_election/<str:id>',views.edit_election,name="edit_election"),
    path('Teacher/',views.Teacher,name="Teacher"),
     path('delete_student/<str:id>',views.delete_student,name="delete_student"),
     path('Assign_ElectionTeacher/',views.Assign_ElectionTeacher,name="Assign_ElectionTeacher"),
      path('View_AssignedTeacher/',views.Assigned_Teacher,name="View_AssignedTeacher"),
      path('View_Classelection_Result/',views.Classelection_Result,name="View_Classelection_Result"),
      path('View_Collegeelection_Result/',views.Collegeelection_Result,name="View_Collegeelection_Result"),
      path('ViewTeacher_Complaint/',views.Teacher_Complaint,name="ViewTeacher_Complaint"),
      path('ViewStudent_Complaint/',views.Student_Complaint,name="ViewStudent_Complaint"),
      path('ComplaintReply/',views.ComplaintReply,name="ComplaintReply"),
      path('View_RepliedStudentComplaint/',views.RepliedStudentComplaint,name="View_RepliedStudentComplaint"),
      path('View_RepliedTeacherComplaint/',views.RepliedTeacherComplaint,name="View_RepliedTeacherComplaint"),






    path('ajaxcourse/',views.ajaxcourse,name="ajaxcourse"),
    path('HomePage/',views.HomePage,name="Homepage"),
]
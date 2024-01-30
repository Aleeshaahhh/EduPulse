from django.urls import path,include
from Teacher import views

app_name="webteacher"

urlpatterns = [
     path('Complaint/',views.Complaint),
    path('EditProfile/',views.EditProfile,name="Editprofile"),

    path('Feedback/',views.Feedback),
    path('HomePage/',views.HomePage,name="Homepage"),
    path('MyProfile/',views.MyProfile,name="MyProfile"),
    path('changepass/',views.changepass,name="changepass"),
    path('NewStudent/',views.NewStudent,name="NewStudent"),
    path('accept_student/<str:id>',views.accept_student,name="accept_student"),
    path('reject_student/<str:id>',views.reject_student,name="reject_student"),
    path('ViewClasscandidate/',views.class_candidate,name="ViewClasscandidate"),
    path('accepted_student/',views.accepted_student,name="accepted_student"),
    path('rejected_student/',views.rejected_student,name="rejected_student"),
    path('Approved_class_candidate/',views.Approved_class_candidate,name="Approved_class_candidate"),
    path('Rejected_class_candidate/',views.Rejected_class_candidate,name="Rejected_class_candidate"),
    path('View_college_candidate/',views.college_candidate,name="View_college_candidate"),
    path('Verified_college_candidate/',views.Verified_college_candidate,name="Verified_college_candidate"),
    path('Rejected_college_candidate/',views.Rejected_college_candidate,name="Rejected_college_candidate"),
    path('View_Reply/',views.View_Reply,name="View_Reply"),
    path('View_Collegepolling/',views.College_Polling,name="View_Collegepolling"),
    path('View_Classpolling/',views.Class_Polling,name="View_ClassPolling"),
    path('accept_class_candidate/<str:id>',views.accept_class_candidate,name="accept_class_candidate"),
    path('reject_class_candidate/<str:id>',views.reject_class_candidate,name="reject_class_candidate"),
    path('verifivote/',views.verifivote,name="verifivote"),
    path('verifing/<str:id>',views.verifing,name="verifing"),





]
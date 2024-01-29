from django.urls import path,include
from Student import views

app_name="webstudent"

urlpatterns = [
     path('Complaint/',views.Complaint,name="Complaint"),
    path('EditProfile/',views.EditProfile,name="Editprofile"),
    path('Feedback/',views.Feedback),
    path('HomePage/',views.HomePage,name="Homepage"),
    path('MyProfile/',views.MyProfile,name="MyProfile"),
    path('changepass/',views.changepass,name="changepass"),
    path('ViewElection/',views.ViewElection,name="ViewElection"),
    path('apply_election/<str:id>',views.apply_election,name="apply_election"),
]
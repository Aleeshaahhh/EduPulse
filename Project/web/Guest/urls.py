from django.urls import path,include
from Guest import views

app_name="webguest"

urlpatterns = [
     path('Login/',views.Login,name="Login"),
    path('Student_Register/',views.Student_Register,name="Student"),
    path('ajaxcourse/',views.ajaxcourse,name="ajaxcourse"),
    path('',views.index,name="index"),

]
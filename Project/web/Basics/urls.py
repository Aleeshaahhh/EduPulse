from django.urls import path,include
from Basics import views
urlpatterns = [
   path('sumoperation/',views.Sum),
   path('calculator/',views.Calculator),
   path('largest/',views.Largest),
   path('Marksheet/',views.Marksheet),
   path('BasicSalary/',views.BasicSalary),
  
]
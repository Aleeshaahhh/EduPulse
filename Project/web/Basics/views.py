from django.shortcuts import render

# Create your views here.
def Sum(request):
    if request.method=="POST":
        num1=int(request.POST.get("txt_number1"))
        num2=int(request.POST.get("txt_number2"))
        sum=num1+num2
        return render(request,"Basics/Sum.html",{'value':result})
    else:
        return render(request,"Basics/Sum.html")

def Calculator(request):
    if request.method=="POST":
        num1=int(request.POST.get("txt_number1"))
        num2=int(request.POST.get("txt_number2"))
        if request.POST.get("btn_res") == "sum":
            result=num1+num2
            return render(request,"Basics/Calculator.html",{'value':result})
        elif request.POST.get("btn_res") == "sub":
            result=num1-num2
            return render(request,"Basics/Calculator.html",{'value':result})
        elif request.POST.get("btn_res") == "mul":
            result =num1*num2
            return render(request,"Basics/Calculator.html",{'value':result})
        elif request.POST.get("btn_res") == "div":
            result =num1/num2
            return render(request,"Basics/Calculator.html",{'value':result})
        else:
            return render(request,"Basics/Calculator.html")
    else:
        return render(request,"Basics/Calculator.html")

def Largest(request):
    if request.method=="POST":
        num1=int(request.POST.get("txt_number1"))
        num2=int(request.POST.get("txt_number2"))
        if num1>num2:
            result=num1
            return render(request,"Basics/Largest.html",{'value':result})
        else:
            result=num2
            return render(request,"Basics/Largest.html",{'value':result})
    else:
        return render(request,"Basics/Largest.html")
def Marksheet(request):
    if request.method=="POST":
        name=request.POST.get("txt_name")
        department=request.POST.get("dept")
        year=request.POST.get("txt_year")
        mark1=int(request.POST.get("txt_number1"))
        mark2=int(request.POST.get("txt_number2"))
        mark3=int(request.POST.get("txt_number3"))
        TotalMark=mark1+mark2+mark3
        Average=TotalMark/3
        if Average>90:
            grade='A+'
        elif Average>80 and Average<=90:
            grade='A'
        elif Average>70 and Average<=80:
            grade='B+'
        elif Average>60 and Averagre<=70:
            grade='B'
        elif Average>50 and Average<=60:
            grade='C'
        elif Average>40 and Average<=50:
            grade='D'
        else: 
            Average<=40
            grade='FAILED'
        return render(request,"Basics/Marksheet.html",{'Name':name,'Department':department,'Year':year,'Mark1':mark1,'Mark2':mark2,'Mark3':mark3,'TotalMark':TotalMark,'Average':Average,'grade':grade})
        
    else:
        return render(request,"Basics/Marksheet.html")
def BasicSalary(request):
    if request.method=="POST":
        FirstName=request.POST.get("txt_fname")
        LastName=request.POST.get("txt_lname")
        name=FirstName+LastName 
        Gender=request.POST.get("gender")
        Marital=request.POST.get("marital")
        Department=request.POST.get("dept")
        BasicSalary=int(request.POST.get("txt_salary"))
        if Gender=='Female' and Marital=='Single':
            name="Miss. "+name
        elif Gender=='Female' and Marital=='Married':
                name="Mrs."+name
        else:
                    name="Mr."+name
        if BasicSalary>=10000:
            TA=0.4*BasicSalary
            DA=0.35*BasicSalary
            HRA=0.3*BasicSalary
            LIC=0.25*BasicSalary
            PF=0.2*BasicSalary
        elif Basicsalary>=5000 and Basicsalary<10000:
            TA=0.35*BasicSalary
            DA=0.3*BasicSalary
            HRA=0.25*BasicSalary
            LIC=0.2*BasicSalary
            PF=0.15*BasicSalary
        elif Basicsalary<5000:
           TA=0.3*BasicSalary
           DA=0.25*BasicSalary
           HRA=0.2*BasicSalary
           LIC=0.15*BasicSalary
           PF=0.10*BasicSalary
        else:
            TA=INVALID
            DA=INVALID
            HRA=INVALID
            LIC=INVALID
            PF=INVALID
        DEDUCTION=LIC+PF
        NETAMOUNT=BasicSalary+TA+DA+HRA-(LIC+PF)
        return render(request,"Basics/BasicSalary.html",{'Name':name,'Gender':Gender,'Marital':Marital,'Department':Department,'BasicSalary':BasicSalary,'TA':TA,'DA':DA,'HRA':HRA,'LIC':LIC,'PF':PF,'DEDUCTION':DEDUCTION,'NETAMOUNT':NETAMOUNT})
    else:
        return render(request,"Basics/BasicSalary.html")

from django.shortcuts import render
from .models import student


# Create your views here.
def index(request):
    students = student.objects.all()
    print("hello")
    return render(request,'index.html',{'students':students})

def search(request):
    print(request.GET["last_name"]=="")
    first_name = request.GET["first_name"]
    last_name =request.GET["last_name"]
    class_name = request.GET["class_name"]
    roll_no = request.GET["roll_no"]
    if first_name!="":
        students = student.objects.filter(first_name=first_name)
    if last_name!="":
        students = student.objects.filter(last_name=last_name)
    if class_name!="":
        students = student.objects.filter(class_name=class_name)
    if roll_no!="":
        students = student.objects.filter(roll_id=roll_no)
    return render(request,'index.html',{'students':students})

from django.shortcuts import render,redirect
from Course.models import course
from Course.form import CourseForm
def home(request):
    Course = course.objects.all()[0:3]
    return render(request, 'home.html',{'course':Course})
def courses(request):
    Course = course.objects.all()
    return render(request, 'courses.html',{'Course':Course})
def addcourses(request):
    form = CourseForm()
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('/courses/')
    else:
        form = CourseForm()
    return render(request, 'addcourses.html', {'form': form})
def aboutus(request):
    return render(request, 'aboutus.html')
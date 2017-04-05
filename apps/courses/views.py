from django.shortcuts import render, redirect
from . models import Course
from ..manager.models import Student

def index(request):
    context= {
        'courses': Course.objects.all()
    }
    return render(request, 'courses/index.html', context)


def add(request):
    # creates new class or stuents to register to


    Course.objects.create(name=request.POST['name'],  description=request.POST['description'])

    return redirect('manager:home')

def join(request, id):


    user_id = request.session['user_id']

    my_course = Course.objects.get(id=id)
    student = Student.objects.get(id=user_id)
    my_course.students.add(student)
    my_course.save()

    return redirect('manager:home')


def edit(request, id):
    # not running edit capability yet

    if request.method == "GET":
        course = Course.objects.get(id=id)
        context= {
            'courses': Course.objects.filter(id=id)
        }


        return render(request, 'courses/edit.html', context)

    if request.method == "POST":

        course = Course.objects.get(id=id)
        course.name = request.POST['name']
        course.description = request.POST['description']
        course.save()


        return redirect('manager:home')

def drop(request, id):


    user_id = request.session['user_id']

    my_course = Course.objects.get(id=id)
    student = Student.objects.get(id=user_id)
    my_course.students.remove(student)
    my_course.save()


    return redirect('manager:home')



def remove(request, id):
    context= {
        'courses': Course.objects.filter(id=id)
    }
    course = Course.objects.get(id=id)

    return render(request, 'courses/remove.html', context)


def confirm(request, id):


    course = Course.objects.get(id=id)

    course.delete()

    return redirect('manager:home')

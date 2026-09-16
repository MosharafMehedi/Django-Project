from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Student
from .forms import StudentForm


def home(request):

    students = Student.objects.all()

    return render(request, 'users/home.html', {
        'students': students,
    })


def create_student(request):

    if request.method == 'POST':

        form = StudentForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Student created successfully!'
            )

            return redirect('home')

    else:
        form = StudentForm()

    return render(request, 'users/create.html', {
        'form': form,
    })


def edit_student(request, id):

    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':

        form = StudentForm(
            request.POST,
            instance=student
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Student updated successfully!'
            )

            return redirect('home')

    else:

        form = StudentForm(instance=student)

    return render(request, 'users/edit.html', {
        'form': form,
    })


def delete_student(request, id):

    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':

        student.delete()

        messages.success(
            request,
            'Student deleted successfully!'
        )

        return redirect('home')

    return redirect('home')
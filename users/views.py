from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.shortcuts import redirect

from .models import Student
from .forms import StudentForm
from .forms import StudentForm, RegisterForm
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout


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

class RegisterView(CreateView):

    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = '/'

    def form_valid(self, form):

        response = super().form_valid(form)

        login(self.request, self.object)

        messages.success(
            self.request,
            'Registration successful!'
        )

        return response
class UserLoginView(LoginView):

    template_name = 'users/login.html'

    redirect_authenticated_user = True

def user_logout(request):

    logout(request)

    messages.success(
        request,
        'You have been logged out.'
    )

    return redirect('login')
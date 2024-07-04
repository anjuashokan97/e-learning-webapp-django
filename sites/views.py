from django.shortcuts import render, redirect
from .models import Course, Booking, CourseBook, Video,Enrollment,Trainer
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


# Create your views here.
def front(request):
    return render(request, 'frt.html')

def home(request):
    return render(request, 'home.html')


def about(request):
    dict_cou = {
        'cou': Course.objects.all()
    }
    return render(request, 'about.html', dict_cou)


def trainer(request):
    dict_tra = {
        'trainer': Trainer.objects.all()
    }
    return render(request, 'trainer.html', dict_tra)


def booking(request):
    course = CourseBook.objects.filter(status='PUBLISH').order_by('-id')
    context = {
        'course' : course,
    }
    return render(request, 'booking.html', context)


def contact(request):
    return render(request, 'contact.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # Get the course name from the form
            course_name = form.cleaned_data.get('cou_name') 

            # Create an Enrollment instance
            enrollment = Enrollment(cou_name=course_name, user=request.user)
            enrollment.save()

    form = RegisterForm()
    dict_form = {
        'form': form
    }
    return render(request, 'register.html', dict_form)


def course_details(request,slug):
    course = CourseBook.objects.filter(slug=slug)
   
    if course.exists():
        course = course.first()
    else:
        return redirect('404')
    context = {
        "course" : course,
        'videos':Video.objects.filter(cou_name=course)
    }
    return render(request, 'course_details.html',context)

def error(request):
    return render(request, 'error.html')


def loginz(request):
    if request.method == 'POST':
        email = request.POST.get('name')
        pass1 = request.POST['pswd']

        mail = User.objects.get(email=email.lower()).username
        user = authenticate(request, username=mail, password=pass1)
        if user is not None:
            login(request, user)
            #messages.success(request, "Successfully Login")
            return redirect('homez')

        else:
            messages.success(request, "Invalid username and Password")
            return redirect('file')
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        uname = request.POST['name']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 != pass2:
            messages.success(request, "Your password is incorrect")
            return redirect('sign')

        else:
            myuser = User.objects.create_user(username=uname, email=email, password=pass1)
            myuser.save()
            messages.success(request, "Successfully Created")
            return redirect('web')
            # return HttpResponse("<h1></h1>")
    return render(request, 'signup.html')


def enrolled_courses(request):

    courses = Enrollment.objects.filter(user=request.user)
    context = {
        'courses' : courses,
    }
    return render(request, 'enrollment.html', context)

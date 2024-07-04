from django.urls import path
from . import views

urlpatterns = [
    path('', views.front, name='web'),
    path('home', views.home, name='homez'),
    path('about', views.about, name='about'),
    path('trainer', views.trainer, name='trainer'),
    path('booking', views.booking, name='booking'),
    path('contact', views.contact, name='contact'),
    path('register', views.register, name='register'),
    path('course/<slug:slug>', views.course_details, name='course_details'),
    path('err', views.error, name='404'),
    path('file', views.loginz, name='file'),
    path('sign', views.signup, name='sign'),
    path('enrollement', views.enrolled_courses, name='enrolled_courses')
]
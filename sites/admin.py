from django.contrib import admin
from . models import Course, Trainer, Booking, Contact, Register, CourseBook, Video
# Register your models here.

class ResumeAdmin(admin.ModelAdmin):
    list_display = ('Candidate_name', 'Phone_No', 'DOB', 'Gender', 'State', 'cou_name', 'cou_type', 'ava_branch', 'Email', 'Qualification','ref')

class VideoAdmin(admin.TabularInline):
    model = Video


class CourseAdmin(admin.ModelAdmin):
    inlines = [VideoAdmin]

admin.site.register(Course)
admin.site.register(Trainer)
admin.site.register(Booking)
admin.site.register(Contact)
admin.site.register(Register, ResumeAdmin)
admin.site.register(CourseBook, CourseAdmin)
admin.site.register(Video)





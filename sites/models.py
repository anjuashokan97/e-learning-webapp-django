from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
# Create your models here.


STATE_CHOICE = (
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Goa', 'Goa'),
    ('Gujarat', 'Gujarat'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jammu and Kashmir', 'Jammu and Kashmir'),
    ('Jharkhand', 'Jharkhand'),
    ('Karnataka', 'Karnataka'),
    ('Kerala', 'Kerala'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Telangana', 'Telangana'),
    ('Tripura', 'Tripura'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('West Bengal', 'West Bengal')
)


class Course(models.Model):
    cou_name = models.CharField(max_length=100)
    cou_description = models.TextField()

    def __str__(self):
        return self.cou_name


class Trainer(models.Model):
    trainer_name = models.CharField(max_length=255)
    cou_name = models.ForeignKey(Course, on_delete=models.CASCADE)
    position = models.CharField(max_length=255)
    image = models.ImageField(upload_to='trainer')


class Booking(models.Model):
    cou_name = models.ForeignKey(Course, on_delete=models.CASCADE)
    starting_date = models.DateField()
    ending_date = models.DateField()
    image = models.ImageField(upload_to='booking')


class Contact(models.Model):
    Candidate_name = models.CharField(max_length=255)
    Phone_No = models.CharField(max_length=10)
    Email = models.EmailField()
    DOB = models.DateField()
    gender = models.CharField(max_length=100)
    Place = models.CharField(max_length=255)
    Qualification = models.CharField(max_length=200)
    cou_name = models.ForeignKey(Course, on_delete=models.CASCADE)
    Willing_time = models.TimeField()
    Booked_on = models.DateField(auto_now=True)


class Register(models.Model):
    Candidate_name = models.CharField(max_length=255)
    Phone_No = models.PositiveIntegerField()
    DOB = models.DateField(auto_now=False, auto_now_add=False)
    Gender = models.CharField(max_length=100)
    State = models.CharField(choices=STATE_CHOICE, max_length=50)
    cou_name = models.ForeignKey(Course, on_delete=models.CASCADE)
    cou_type = models.CharField(max_length=100)
    ava_branch = models.CharField(max_length=150)
    Email = models.EmailField()
    Qualification = models.CharField(max_length=200)
    ref = models.CharField(max_length=200)


class CourseBook(models.Model):
    STATUS = (
        ('PUBLISH','PUBLISH'),
        ('DRAFT', 'DRAFT'),
    )

    ONE_TO_FIVE_RATING_CHOICES = (
    (0, '0'),
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)

    image = models.ImageField(upload_to="booking",null=True)
    cou_name = models.ForeignKey(Course, on_delete=models.CASCADE)
    rate = models.IntegerField(choices=ONE_TO_FIVE_RATING_CHOICES,null=True)
    price = models.IntegerField(null=True,default=0)
    discount = models.IntegerField(null=False)
    slug = models.SlugField(default='', max_length=500, null=True, blank=True)
    status = models.CharField(choices=STATUS,max_length=100,null=True)


    def __str__(self):
         return str(self.cou_name)


    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("course_details", kwargs={'slug': self.slug})



def create_slug(instance, new_slug=None):
    slug = slugify(instance.cou_name)
    if new_slug is not None:
        slug = new_slug
    qs = CourseBook.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, CourseBook)


class Video(models.Model):
    cou_name = models.ForeignKey(CourseBook, on_delete=models.CASCADE)
    serial_number = models.IntegerField(null=False)
    heading = models.CharField(max_length=100,null=False)
    video = models.FileField(upload_to="video",null=False)

    def __str__(self):
        return f"{self.cou_name.cou_name}- {self.heading}"




    


    

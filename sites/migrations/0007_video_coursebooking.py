# Generated by Django 4.1.7 on 2024-01-25 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0006_contact_gender_register_ava_branch_register_cou_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.IntegerField()),
                ('heading', models.CharField(max_length=100)),
                ('video', models.FileField(upload_to='video')),
                ('cou_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.course')),
            ],
        ),
        migrations.CreateModel(
            name='CourseBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='booking')),
                ('rate', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True)),
                ('price', models.IntegerField(default=0, null=True)),
                ('discount', models.IntegerField(null=True)),
                ('slug', models.SlugField(blank=True, default='', max_length=500, null=True)),
                ('status', models.CharField(choices=[('PUBLISH', 'PUBLISH'), ('DRAFT', 'DRAFT')], max_length=100, null=True)),
                ('cou_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.course')),
            ],
        ),
    ]

from django import forms
from .models import Register


class DateInput(forms.DateInput):
    input_type = 'date'


GENDER_CHOICE = [
    ('Male', 'Male'),
    ('Female', 'Female')
]

COURSE_TYPE = [
    ('Basics Course(12 days)', 'Basics Course(12 days)'),
    ('Advanced Course(30 days)', 'Advanced Course(30 days)')
]

AVA_BRA = [
    ('Tvm', 'Tvm'),
    ('Pune', 'Pune'),
    ('Calicut', 'Calicut'),
    ('Delhi', 'Delhi')
]


class RegisterForm(forms.ModelForm):
    Gender = forms.ChoiceField(choices=GENDER_CHOICE, widget=forms.RadioSelect)
    cou_type = forms.ChoiceField(label='Course Mode', choices=COURSE_TYPE, widget=forms.RadioSelect)
    ava_branch = forms.MultipleChoiceField(label='Available Branches', choices=AVA_BRA, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Register
        fields = '__all__'

        labels = {
            'Candidate_name': 'Candidate Name',
            'Phone_No': 'Contact Number',
            'DOB': 'Date of Birth',
            'Gender': 'Gender',
            'State': 'State',
            'cou_name': 'Selective Course',
            'cou_type': 'Course Mode',
            'ava_branch': 'Available Branches',
            'Email': 'Email ID',
            'Qualification': 'Qualification',
            'ref': 'How you learn about this site'
        }

        widgets = {
            'Candidate_name': forms.TextInput(attrs={'class': 'form-control'}),
            'Phone_No': forms.NumberInput(attrs={'class': 'form-control'}),
            'DOB': DateInput(attrs={'class': 'form-control'}),
            'Gender': forms.RadioSelect(attrs={'class': 'form-control'}),
            'State': forms.Select(attrs={'class': 'form-control'}),
            'cou_name': forms.Select(attrs={'class': 'form-control'}),
            'cou_type': forms.TextInput(attrs={'class': 'form-control'}),
            'ava_branch': forms.TextInput(attrs={'class': 'form-control'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control'}),
            'Qualification': forms.TextInput(attrs={'class': 'form-control'}),
            'ref': forms.TextInput(attrs={'class': 'form-control'})
        }

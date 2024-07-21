from django import forms
from .models import Blog
from course.models import Speciality

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'image', 'status', 'comment']

class BlogUpdateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'status', 'comment', 'publish']




class SpecialityForm(forms.ModelForm):
    class Meta:
        model = Speciality
        fields = ['title', 'slug', 'course']

class SpecialityUpdateForm(forms.ModelForm):
    class Meta:
        model = Speciality
        fields = ['title', 'slug', 'course', 'created_at']
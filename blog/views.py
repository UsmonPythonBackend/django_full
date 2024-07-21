from django.shortcuts import render,redirect,get_object_or_404
from .models import Blog
from course.models import Speciality
from .forms import BlogForm,BlogUpdateForm
from django.http import HttpResponse

def blog_view(request):
    blogs = Blog.objects.all()
    specialitys = Speciality.objects.all()
    return render(request, 'blog.html', {"blogs":blogs, "specialitys":specialitys})


def blog_detail_view(request, id):
    blog = Blog.objects.all(id=id)
    specialitys = Speciality.objects.all()
    return render(request, 'blog-detail.html', {'blog':blog})


def blog_create_view(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog-list')

    form = BlogForm()
    return render(request, 'blog_create.html', {'form':form})

def blog_update_view(request,pk):
    blogs = get_object_or_404(Blog, pk=pk)
    if request.method =="POST":
        form = BlogUpdateForm(request.POST, instance=blogs)
        if form.is_valid():
            form.save()
            return redirect('blog-detail', pk=blogs.pk)
        else:
            form = BlogUpdateForm()
            return render(request, "blog_update.html", {'blogs': blogs,"message_error":'Error', 'blogs':blogs})

    blogs = Blog.objects.get(pk=pk)
    return render(request, "blog_update.html", {'blogs':blogs})

def blog_delete_view(request,id):
    blogs = Blog.object.get(id=id)
    blogs.delete()
    return redirect('blog-list')


def speciality_view(request):
    specialitys = Speciality.objects.all()
    return render(request, 'speciality.html', {"specialitys":specialitys})

def speciality_detail_view(request, id):
    specialitys = Speciality.objects.all()
    return render(request, 'speciality-detail.html', {'specialitys':specialitys})

def speciality_create_view(request):
    if request.method =="POST":
        form = SpecialityForm(data=request.POST)
        if form.is_valid():
            specialitys = form.save(commit=False)
            specialitys.image = request.POST['image']
            specialitys.save()
            return redirect('speciality-list')
    form = BlogForm()
    return render(request, 'speciality_create.html', {'form':form})

def speciality_update_view(request,pk):
    specialitys = get_object_or_404(Speciality, pk=pk)
    if request.method =="POST":
        form = SpecialityUpdateForm(request.POST, instance=specialitys)
        if form.is_valid():
            form.save()
            return redirect('speciality-detail', pk=specialitys.pk)
        else:
            form = SpecialityUpdateForm()
            return render(request, "speciality_update.html", {'specialitys': specialitys,"message_error":'Error', 'specialitys':specialitys})

    specialitys = Speciality.objects.get(pk=pk)
    return render(request, "speciality_update.html", {'specialitys':specialitys})


def speciality_delete_view(request,id):
    specialitys = Speciality.object.get(id=id)
    specialitys.delete()
    return redirect('speciality-list')

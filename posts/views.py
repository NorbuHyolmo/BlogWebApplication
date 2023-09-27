from django.shortcuts import render, redirect
from .models import Post
from django.contrib import messages

# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, "index.html", {"posts": posts})


def post(request, id):
    posts = Post.objects.get(id=id)
    return render(request, 'post.html', {'posts': posts})


def update(request, id):
    data = Post.objects.get(pk=id)
    if request.method=="POST":
        title = request.POST['title']
        wake_up = request.POST['wake_up']
        coding_hours_start = request.POST['coding_hours_start']
        coding_hours_end = request.POST['coding_hours_end']
        exercise = request.POST['exercise']
        remarks = request.POST['remarks']
        # created_at = request.POST['created_at']

        data = Post(id=id, title=title, wake_up=wake_up, coding_hours_start=coding_hours_start, coding_hours_end= coding_hours_end , exercise=exercise, remarks=remarks)
        data.save()
        messages.info(request, "Blog Updated!")

    return render(request, "update.html", {'data':data})

# def add_blog(request):
#     return render(request, "add_blog.html")


def delete(request, id):
    data = Post.objects.get(id=id)
    data.delete()
    return redirect("index")

def add(request):
    if request.method=="POST":
        title = request.POST['title']
        wake_up = request.POST['wake_up']
        coding_hours_start = request.POST['coding_hours_start']
        coding_hours_end = request.POST['coding_hours_end']
        exercise = request.POST['exercise']
        remarks = request.POST['remarks']
        # created_at = request.POST['created_at']

        data = Post(title=title, wake_up=wake_up, coding_hours_start=coding_hours_start, coding_hours_end= coding_hours_end , exercise=exercise, remarks=remarks)
        data.save()
        messages.info(request, "New Blog Saved!")


    return render(request, "Add.html")

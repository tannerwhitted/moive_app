from django.shortcuts import render, redirect, HttpResponse
from apps.project_app.models import *

from django.contrib import messages

from django.core.files.uploadedfile import SimpleUploadedFile


def index(request):
    return render(request, 'project_app/index.html')


def register(request):
    return render(request, 'project_app/register.html')


def add_user(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect ('/register')
    if request.POST['password'] == request.POST['confirm_password']:
        new_user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = request.POST['password']
        )
        request.session['user'] = new_user.first_name
        request.session['id'] = new_user.id
        return redirect('/success')
    else:
        messages.error(request, "Passwords didn't match")
        return redirect('/register')


def login(request):
    logged_user = User.objects.filter(email=request.POST['email'])
    if logged_user[0]:
        if logged_user[0].password == request.POST['password']:
            request.session['user'] = logged_user[0].first_name
            request.session['id'] = logged_user[0].id
            return redirect('/success')
        else:
            return redirect('/')


def logout(request):
    request.session.flush()
    return redirect('/')

def success(request):
    context = {
        "user": User.objects.all(),
        "this_user": User.objects.get(id=request.session['id']),
        "review": Review.objects.all(),
    }

    return render(request, 'project_app/home.html', context)

def search(request):
    last_movie = Movie.objects.last()
    scale = int(last_movie.id) - 3
    search = request.POST['search']
    search_list = search.split(' ')
    search_results = []
    for word in search_list:
        search_results.append(Movie.objects.filter(title__contains=word))
    context = {
        "results": search_results,
        "movies": Movie.objects.all(),
        "this_user": User.objects.get(id=request.session['id']),
        "users": User.objects.all(),
        "scale": scale
    }
    return render(request, 'project_app/search.html', context)

def profile(request, user_id):
    context = {
        "this_user": User.objects.get(id=request.session['id']),
        "user": User.objects.get(id=user_id),
        "movie": Movie.objects.all(),
        "review": Review.objects.all()
    }
    return render(request, 'project_app/user.html', context)

def add_movie(request):
    context = {
        "user": User.objects.get(id=request.session['id'])
    }
    return render(request, 'project_app/add_movie.html', context)

def add_movie_process(request):
    errors = Movie.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect ('/add_movie')
    new_movie = Movie.objects.create(
        title = request.POST['title'],
        desc = request.POST['desc'],
        run_time = request.POST['run_time'],
        released_at = request.POST['released_at'],
        cast = request.POST['cast']
    )
    return redirect('/success')

def this_movie(request, movie_id):
    context = {
        "movie": Movie.objects.get(id=movie_id),
        "user": User.objects.all(),
        "this_user": User.objects.get(id=request.session['id'])
    }
    return render(request, 'project_app/this_movie.html', context)

def add_review(request, movie_id):
    new_review = Review.objects.create(
        rating = request.POST['rating'],
        review = request.POST['review'],
        movie = Movie.objects.get(id=movie_id),
        user = User.objects.get(id=request.session['id'])
    )
    return redirect('/this_movie/' + movie_id)

def delete(request, review_id, movie_id):
    this_review = Review.objects.get(id=review_id)
    this_review.delete()

    return redirect('/this_movie/' + movie_id)

def delete_from_home(request, review_id, movie_id):
    this_review = Review.objects.get(id=review_id)
    this_review.delete()
    return redirect('/success')
    
def delete_from_user(request, review_id, user_id):
    this_review = Review.objects.get(id=review_id)
    this_review.delete()
    return redirect('/profile/' + user_id)

def add_user_image(request, user_id):
    if request.method == 'POST':
        this_user = User.objects.get(id=user_id)
        this_user.pic = request.FILES['pic']
        this_user.save()
        print(this_user.pic)
        return redirect('/profile/' + user_id)
    else:
        form = User()
    return render(request, 'upload.html', {'form': form})

def add_movie_image(request, movie_id):
    if request.method == 'POST':
        this_movie = Movie.objects.get(id=movie_id)
        this_movie.pic = request.FILES['pic']
        this_movie.save()
        print(this_movie.pic)
        return redirect('/this_movie/' + movie_id)
    else:
        form = Movie()
    return render(request, 'upload.html', {'form': form})
from __future__ import unicode_literals
from django.db import models


class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 1:
            errors['first_name'] = "First name must be at least one character"
        if len(postData['last_name']) < 1:
            errors['last_name'] = "Last name must be at least one character"
        if len(postData['password']) < 6:
            errors['password'] = "Password must be at least six characters"
        email = postData['email']
        if '@' not in email:
            errors['email'] = "Not a valid email address"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    pic = models.FileField(upload_to='documents/%Y/%m/%d', default="/static/project_app/images/34AD2.jpg")
    bio = models.CharField(max_length=255, default ="")
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    follow = models.ManyToManyField("User", related_name="following")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class MovieManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 1:
            errors['title'] = "Not a valid title"
        if len(postData['desc']) < 5:
            errors['desc'] = "You can say more than that about this movie"
        if len(postData['run_time']) > 3:
            errors['run_time'] = "No movie's that long"
        if len(postData['released_at']) != 4:
            errors['released_at'] = "Not a valid release year"
        if len(postData['cast']) < 15:
            errors['cast'] = "More than one guy was in this"
        return errors
    
class Movie(models.Model):
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    run_time = models.IntegerField(default=1)
    released_at = models.IntegerField(default=1)
    cast = models.CharField(max_length=255)
    pic = models.FileField(upload_to='documents/%Y/%m/%d', default='static/project_app/images/reel.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MovieManager()


class Review(models.Model):
    rating = models.IntegerField(default=1)
    review = models.CharField(max_length=255)
    movie = models.ForeignKey(Movie, related_name="movie")
    user = models.ForeignKey(User, related_name="user")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
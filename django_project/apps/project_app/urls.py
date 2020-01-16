from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^add_user$', views.add_user),
    url(r'^success$', views.success),
    url(r'^logout$', views.logout),
    url(r'^search$', views.search),
    url(r'^profile/(?P<user_id>\d+)$', views.profile),
    url(r'^add_movie$', views.add_movie),
    url(r'^add_movie_process$', views.add_movie_process),
    url(r'^this_movie/(?P<movie_id>\d+)$', views.this_movie),
    url(r'^add_review/(?P<movie_id>\d+)$', views.add_review),
    url(r'^delete/(?P<review_id>\d+)/(?P<movie_id>\d+)$', views.delete),
    url(r'^delete_from_home/(?P<review_id>\d+)/(?P<movie_id>\d+)$', views.delete_from_home),
    url(r'^delete_from_user/(?P<review_id>\d+)/(?P<user_id>\d+)$', views.delete_from_user),
    url(r'^action_page/(?P<user_id>\d+)$', views.add_user_image),
    url(r'^movie_pic/(?P<movie_id>\d+)$', views.add_movie_image),

] 

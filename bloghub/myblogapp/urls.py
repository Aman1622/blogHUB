from django.urls import path
from . import views

app_name="myblogapp"

urlpatterns= [
    path("",views.home,name="home_hai"),
    path("blog/create/",views.add_blog,name="add_blog"),
    path("blog/",views.index, name="index"),
    path("blog/<int:myblog_id>/",views.detail,name='detail'),
    path("blog/update/<int:myblog_id>/",views.update,name='update'),
    path("blog/delete/<int:myblog_id>/",views.delete,name="delete_now"),
    path("blog/rating/<int:myblog_id>/",views.give_rating,name="give_rating"),
    path("blog/top_rated/",views.top_rated,name="top_rated_blogs"),
]
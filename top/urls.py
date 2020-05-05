from django.urls import path
from top.views import UserListView
from . import views

urlpatterns = [
    path('index/', views.index,name='index'),
    path('about/',views.about,name='about'),
    path('expect/', views.expect, name='expect'),
    path('unable/', views.unable, name='unable'),
    path('possible/', views.possible, name='possible'),
    path('filter/',UserListView.as_view())

]
#->index/ = to post the data in url


#->about/ = for list out the title of jobs
#->expect/ = to view whole data
#->unable/?id= = to filter the data using id
#->possible/ = to filter the data using title and location in json view (function base)
#->filter/ = to filter the data using title and location in api view (class base)

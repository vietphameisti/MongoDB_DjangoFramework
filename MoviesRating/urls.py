"""
Definition of urls for MoviesRating.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from MovieCRUD.views import moviesintheaters_view
from MovieCRUD.views import moviesingle_view
from MovieCRUD.views import addComment_view
from MovieCRUD.views import search_view
from MovieCRUD.views import loginpage,logout,profile
from MovieCRUD.views import signup
from MovieCRUD.views import topsearch_view
urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    #path('', moviesintheaters_view, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    path('moviegrid/',moviesintheaters_view, name='viewall'),
    path('moviesingle/<int:movieID>/',moviesingle_view), 
    path('moviegrid/moviesingle/<int:movieID>/',moviesingle_view),
    path('search/moviesingle/<int:movieID>/', moviesingle_view),
    
    path('addComment/<int:movieID>/', addComment_view),
    
    path('search/', search_view),
    path('topsearch/', topsearch_view),
    path('moviegrid/topsearch/', topsearch_view),
   
    path('signin/', loginpage, name='loginpage'),
    path('signin/home', views.home, name='home'),
    path('admin/index', admin.site.urls, name='adminsignin'),
    #path('signin/profile/', profile, name='profile'),
    path('profile/', profile, name='profile'),
    path('signup/', signup, name='signup'),
    path('signup/home', views.home, name='home'),
    path('logout/', logout, name='logout'),
]

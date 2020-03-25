from django.shortcuts import render
from django.core.paginator import Paginator

from .models import moviesintheaters
from .models import contentRate
from .models import Rating

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
#from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login as auth_login
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm



def moviesintheaters_view(request,*args,**kwargs):
    moviesintheaters_list=moviesintheaters.objects.order_by('-imdbRating').all()
    #paginator=Paginator(moviesintheaters_list,20)
    #page=request.GET.get('testDisplay.html')
    #moviesintheaters_list=paginator.page(paginator.num_pages)
    #print(moviesintheaters_list)
    context={'moviesintheaters_list':moviesintheaters_list}
    return render(request,"app/moviegrid.html",context)
    #return render(request,'app/index.html',context)

#movieID   
def moviesingle_view(request,movieID):
    movieTitle = moviesintheaters.objects.get(id=movieID)
    movie = moviesintheaters.objects.filter(title__icontains = movieTitle)

#    numbComment=movie.contentRating.count()
    
    return render(request, "app/moviesingle.html", {'movie': movie})

   
def addComment_view(request, movieID):
    if request.method == 'POST':
        comment = contentRate()
        comment.content = request.POST['message']

        rate = Rating()
        rate.ratingValue = request.POST['ratingValue']

        newMovie = moviesintheaters.objects.get(pk=movieID)
        newMovie.contentRating.append(comment)
        newMovie.ratings.append(rate)
        newMovie.save()

    movieTitle = moviesintheaters.objects.get(id=movieID)
    movie = moviesintheaters.objects.filter(title__icontains=movieTitle)
    return render(request, "app/moviesingle.html", {'movie': movie})


def search_view(request):
    #movies = moviesintheaters.objects.all()
    if request.method == 'GET':
        movieTitle = request.GET.get('title_search')
        fromYear=  request.GET.get('fromyear_search')
        toYear = request.GET.get('toyear_search')
        if (movieTitle == None) and (fromYear == None) and(toYear==None):
            movies = moviesintheaters.objects.all()
        elif (request.GET.get('title_search')):
            movies = moviesintheaters.objects.filter(title__icontains=movieTitle)
        elif(request.GET.get('fromyear_search')):
            movies = moviesintheaters.objects.filter(year__gte=fromYear)
        elif (request.GET.get('toyear_search')):
            movies = moviesintheaters.objects.filter(year__lt=toYear)
    #else:
    #    movies = moviesintheaters.objects.all()

    return render(request, 'app/movielist.html', {'movies': movies})


def topsearch_view(request):
    #movies = moviesintheaters.objects.all()
    if request.method == 'GET':
        movieTitle = request.GET.get('topsearch')
        if movieTitle == None:
            movies = moviesintheaters.objects.all()
        else :
            movies = moviesintheaters.objects.filter(title__icontains=movieTitle)        
    #else:
    #    movies = moviesintheaters.objects.all()

    return render(request, 'app/movielist.html', {'movies': movies})

def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password =  request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                auth_login(request, user)
                if user.is_superuser:
                    #return HttpResponse(reverse('admin'))
                    #return HttpResponseRedirect(request.POST['next'])
                    return HttpResponseRedirect('/admin/index')
                else:
                    username = request.POST['username']
                    request.session['username'] = username
                    return HttpResponseRedirect("home")

        #post = User.objects.filter(username=username)
        #if post:
        #    username = request.POST['username']
        #    request.session['username'] = username
        #    print(username)
        #    return HttpResponseRedirect("home")
        else:
            return render(request, 'app/index.html', {})
    return render(request, 'app/index.html', {})

#def profile(request):
#    if request.session.has_key('username'):
#        posts = request.session['username']
#        query = User.objects.filter(username=posts) 
#        return render(request, 'app/userprofile.html', {"query":query})
#    elif request.user.is_authenticated:
#        query = request.user.username
#        return render(request, 'app/userprofile.html', {"query":query})
#    else:
        
#        return render(request, 'app/index.html', {})
def profile(request):
    if request.user.is_authenticated:
        posts = request.user.username
        query = User.objects.filter(username=posts)
        return render(request, 'app/userprofile.html', {"query":query})
    else:
        return render(request, 'app/index.html', {})

def logout(request):
    try:
        del request.session['username']
    except:
        pass
    return render(request, 'app/index.html', {})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return HttpResponseRedirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'app/signup.html', {'form': form})


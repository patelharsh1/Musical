from django.shortcuts import render , redirect
from django.contrib import  messages
from .models import *
# Create your views here.

def index3page(request):
    return render(request,"index3.html")

def indexpage(request):
    return render(request,"index.html")

def index2page(request):
    try:
        uid = request.session["logid"]
        checkid = REGISTER.objects.get(id=uid)
        context = {
            "logdata": checkid
        }
        return render(request, 'index2.html', context)
    except KeyError:
        # Handle the case when 'logid' is not present in the session
        pass
    except REGISTER.DoesNotExist:
        # Handle the case when the object with the specified ID is not found
        pass

    return render(request, "index2.html")


def favouritepage(request):
    return render(request,"favourite.html")

def pricing_plan(request):
    return render(request,"pricing_plan.html")

def add_playlist(request):

    uid = request.session["logid"]

    try:
        getplaylist = PLAYLIST.objects.get(USER_ID=uid)
        context = {
            "playlistname": getplaylist
        }
        # return redirect("/add_playlist.html",context)
        return render(request, "add_playlist.html",context)
    except:
        pass
    return render(request,"add_playlist.html")

def free_music(request):
    getmusic = MUSIC.objects.all()

    context = {
        "musicdata" : getmusic
    }
    return render(request,"free_music.html",context)

def genres_single(request):
    return render(request,"genres_single.html")

def registeruser(request):
    name = request.POST.get("first_name")
    Email = request.POST.get("email")
    password = request.POST.get("password")
    rePassword = request.POST.get("confirm_password")
    dob = request.POST.get("date_of_birth")
    tele = request.POST.get("phone")
    dp = request.FILES["profile_picture"]
    gender = request.POST.get("gender")


    try:
        checkuser = REGISTER.objects.get(EMAIL=Email)
    except:
        checkuser = None

    if checkuser is None:

        adduser = REGISTER(NAME=name,EMAIL=Email,PASSWORD=password,
                           repassword=rePassword,DOB=dob,PHONE=tele,DP=dp,GENDER=gender)
        adduser.save()
        messages.success(request,"Thank you For login ....")
    else:
        messages.error(request,"please create account....")

    return render(request,"index2.html")

def loginuser(request):
    Email = request.POST.get("email")
    password = request.POST.get("password")
    try:
        checkuser = REGISTER.objects.get(EMAIL=Email,PASSWORD=password)
        request.session["logid"] = checkuser.id
        request.session["logname"] = checkuser.NAME
        request.session.save()
    except:
        checkuser = None

    if checkuser is not None:
        return redirect("/")
    else:
        messages.success(request,"please enter right details...")
    return redirect("/")

def logout(request):
    request.session.pop("logid", None)
    request.session.pop("logname", None)
    return redirect("/")

def artistregister(request):
    return render(request,"artistregister.html")

def registerartist(request):
    name = request.POST.get("first_name")
    Type = request.POST.get("type")
    dob = request.POST.get("password")
    dp = request.FILES["profile"]


    try:
        checkuser = ARTIST.objects.get(ARTIST_NAME=name)
    except:
        checkuser = None

    if checkuser is None:

        adduser = ARTIST(ARTIST_NAME=name,ARTIST_TYPE=Type,ARTIST_IMAGE=dp,
                           ARTIST_DOB=dob)
        adduser.save()
        # request.session["logaid"] = checkuser.id
        # request.session["loganame"] =  checkuser.ARTIST_NAME
        # request.session.save()
        messages.success(request,"Thank you For login ....")
    else:
        messages.error(request,"please create account....")

    return render(request,"index2.html")

def artist(request):
    artistdata = ARTIST.objects.all()
    context = {
        "artistuser" : artistdata
    }
    return render(request,"artist.html",context)

def artist_single(request,id):
    artistprofile = ARTIST.objects.get(id=id)

    context = {
        "artistdata" : artistprofile
    }
    return render(request,"artist_single.html",context)

def newplaylist(request):
    return render(request,"newplaylist.html")

def playlist(request):
    name = request.POST.get("playlistname1")
    userid = request.session["logid"]
    createplaylist = PLAYLIST(PLAYLIST_NAME=name,id=userid)
    createplaylist.save()

    return render(request,"add_playlist.html")


from __future__ import unicode_literals,absolute_import
from django.shortcuts import render, redirect
from .models import Document, Projet, Short, Vekflix, Youtube, BarreRaccourcie,Stegano,FaceRecognition,Exercice
from django.db.models import Q
from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import FileResponse
from pytube import YouTube
import os
import filetype
from django.core.files.storage import FileSystemStorage
from .forms import DocumentForm, ShortForm, YoutubeForm,SteganoForm,FaceForm
from django.conf import settings
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponse
import sweetify
from wsgiref.util import FileWrapper
import pathlib
import psutil
import datetime
import time
from vacances_scolaires_france import SchoolHolidayDates
from django.core.mail import send_mail
from os import listdir
from os.path import isfile, join
import requests
from url_decode import urldecode
import math
import random,string
from tmdbv3api import TMDb, Movie
import urllib
import os
import requests
from cryptosteganography import CryptoSteganography
from PIL import Image
import cv2
from deeplator import Translator
from thispersondoesnotexist import get_online_person, get_checksum_from_picture, Person,save_picture


def handler404(request, exception, template_name="404.html"):
    response = render_to_response("404.html")
    response.status_code = 404
    return response

def home(request):
    name = 'Home'
    projects = Projet.objects.all().order_by('-created')
    count= Projet.objects.all().count()
    coffees = int(count*12)
    barre = BarreRaccourcie.objects.all()
    cpu = int(psutil.cpu_percent())
    disk_usage = int(psutil.disk_usage('/').percent)
    cpu_freq = int(psutil.cpu_freq().current)
    x = datetime.datetime.now()
    year = int(x.strftime("%y"))
    month = int(x.strftime("%m"))
    day = int(x.strftime("%d"))
    months = []
    projects_months = []
    onemonth = [1,3,5,7,8,10,12]#31 days month
    zeromonth = [4,6,9,11]#30 days month
    strangemonth = 2 #28 or 29 days month (february)
    for i in range(0,7):
        if month-(6-i)<1:
            months.append(12-(6-month-i))
        else:
            months.append(month-(6-i))
    for project in projects:
         projects_months.append(str(project.created)[5:7])

    file = open("holidays.txt", "r+")
    today = datetime.date(2000 + year, month, day)
    date = file.readline()
    if str(x)[:10] == str(date)[:10] and False:
        is_holiday = file.readline()
        daysbeforeholiday = int(file.readline())
    else:
        d = SchoolHolidayDates()
        is_holiday = d.is_holiday_for_zone(datetime.date(2000+year, month, day), 'C')
        daysbeforeholiday = 0
        if is_holiday == False:
            while is_holiday == False:
                if month in onemonth and day == 31:
                    month = month+1
                    day=1
                elif month in zeromonth and day == 30:
                    month = month + 1
                    day = 1
                elif month == 2 and day == 28:
                    month = month + 1
                    day = 1
                day = day + 1
                is_holiday = d.is_holiday_for_zone(datetime.date(2000 + year, month, day), 'C')
            holiday_date = datetime.date(2000+year, month, day)
            delta = holiday_date - today
            daysbeforeholiday = delta.days
            is_holiday = False
        open('holidays.txt', 'w').close()
        file = open("holidays.txt", "r+")
        file.write('%s\n' % datetime.datetime.now())
        #file.write(datetime.datetime.now().strftime("%H:%M:%S") + os.linesep)
        file.write('%s\n' % is_holiday)
        file.write('%s\n' % daysbeforeholiday)
    return render(request, 'index.html', {'projects':projects,'count': count, "barre": barre, 'cpu': cpu, 'disk': disk_usage, 'cpu_freq': cpu_freq, 'months': months, 'projects_months': projects_months, 'name': name, 'is_holiday': is_holiday, 'daysbeforeholiday': daysbeforeholiday,'coffees': coffees})


def new(request):
    return render(request, 'base_new.html')


def projects(request):
    name = 'Projects'
    projects = Projet.objects.all().order_by('-created')
    barre = BarreRaccourcie.objects.all()
    return render(request, '../templates/project.html', {'projects':projects, "barre": barre, 'name': name})


def project(request, url):
    name = 'Projects'
    content = Projet.objects.get(url=url)
    others = Projet.objects.all().order_by('-created')
    barre = BarreRaccourcie.objects.all()
    return render(request, '../templates/work-single.html', {'projet':content,'others':others, 'barre': barre, 'name': name})

def file_projects(request, url, file):
    stream = open('media/projets/' + str(file), 'rb')
    response = FileResponse(stream)
    return response

@login_required(login_url='/admin/')
def delete_folder(request, folder):
    if request.method == 'POST':
        doc = Document.objects.filter(folder=folder)
        path = "media/"
        for file in doc:
            os.remove(path+str(file.file.name))
        doc.delete()
    return redirect('cloud')

@login_required(login_url='/admin/')
def delete_file(request, pk):
    if request.method == 'POST':
        doc = Document.objects.filter(pk=pk)
        path = "media/"
        for file in doc:
            os.remove(path + str(file.file.name))
        doc.delete()
    return redirect('cloud')


def cloud(request):
    barre = BarreRaccourcie.objects.all()
    documents = Document.objects.all().order_by('file')
    name = "Folders"
    a = []
    index = []
    i = 0
    for item in documents:
        if item.folder in a:
            index.append(i)
        else:
            a.append(item.folder)
        i += 1
    return render(request, 'cloud/cloud.html', { 'documents': documents, 'index': index, "barre": barre, 'name': name})



def files(request, url):
    barre = BarreRaccourcie.objects.all()
    documents = Document.objects.filter(folder=urldecode(url)).order_by('file')
    folder = urldecode(url)
    names = []
    types = []
    name = 'Folders'
    for document in documents:
        names.append(document.file.name[8:])
        if pathlib.Path('media/'+str(document.file.name)).suffix == '.docx' or pathlib.Path('media/'+str(document.file.name)).suffix == '.odt'or  pathlib.Path('media/'+str(document.file.name)).suffix == '.doc':
            types.append('word')
        elif pathlib.Path('media/'+str(document.file.name)).suffix == '.xlx' or pathlib.Path('media/'+str(document.file.name)).suffix == '.xlsx' or pathlib.Path('media/'+str(document.file.name)).suffix == '.csv' or pathlib.Path('media/'+str(document.file.name)).suffix == '.CSV':
            types.append('excel')
        elif pathlib.Path('media/'+str(document.file.name)).suffix == '.apk':
            types.append('android')
        elif pathlib.Path('media/'+str(document.file.name)).suffix == '.rw3':
            types.append('chart-area')
        elif pathlib.Path('media/'+str(document.file.name)).suffix == '.pptx' or pathlib.Path('media/'+str(document.file.name)).suffix == '.ppt':
            types.append('presentation')
        elif filetype.guess("media/"+str(document.file.name)):
            type = filetype.guess("media/"+str(document.file.name))
            types.append(type.mime)
        elif pathlib.Path('media/'+str(document.file.name)).suffix == '.py' or pathlib.Path('media/'+str(document.file.name)).suffix == '.js' or pathlib.Path('media/'+str(document.file.name)).suffix == '.c' or  pathlib.Path('media/'+str(document.file.name)).suffix == '.xml':
            types.append('code')
        elif pathlib.Path('media/'+str(document.file.name)).suffix == '.avi' or pathlib.Path('media/'+str(document.file.name)).suffix == '.mp4' or pathlib.Path('media/'+str(document.file.name)).suffix == '.mkv':
            types.append('video')
        elif pathlib.Path('media/'+str(document.file.name)).suffix == '.html':
            types.append('html5')
        elif pathlib.Path('media/' + str(document.file.name)).suffix == '.css':
            types.append('css3')
        elif pathlib.Path('media/'+str(document.file.name)).suffix == 'log' or pathlib.Path('media/'+str(document.file.name)).suffix == 'config':
            types.append('settings')
        else:
            types.append('file')
    return render(request,'cloud/particular.html' , {'files': documents, 'url': url, 'names': names, 'types': types, "barre": barre, 'name': name, 'folder':folder})

def file_download(request, url, file):
    document = Document.objects.get(file = 'uploads/'+file)
    if request.method == 'POST':
            password = request.POST.get('password')
            if password == document.password:
                stream = open('media/uploads/' + str(file), 'rb')
                response = FileResponse(stream)
                return response
            else:
                return render(request, 'cloud/password_required.html')
    else:
        if document.password:
            wrong_message = 'The password is wrong try again'
            return render(request, 'cloud/password_required.html', {'wrong': wrong_message})
        stream = open('media/uploads/'+str(file), 'rb')
        response = FileResponse(stream)
        return response

def delete(self, *args, **kwargs):
    os.remove(os.path.join(settings.MEDIA_ROOT, self.field_name.name))
    super(TheModel, self).delete(*args, **kwargs)

@login_required(login_url='/admin/')
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        folder = request.POST.get("folder")
        password = request.POST.get("password")
        for f in request.FILES.getlist('file'):
            instance = Document(folder=folder, file=f,password=password)
            instance.save()
        return redirect('cloud')
    else:
        form = DocumentForm()
        barre = BarreRaccourcie.objects.all()
        name = "Upload"
        documents = Document.objects.all().order_by('file')
        documentsFolder = []
        for document in documents:
            if document.folder not in documentsFolder:
                documentsFolder.append(document.folder)
        return render(request, 'cloud/upload.html', {
        'form': form,
        'barre': barre,
        'name': name,
        'documentsFolder':documentsFolder
    })


def short_url(request):
    if request.method == 'POST':
        form = ShortForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            return redirect('short_sucessful', name)
    else:
        form = ShortForm()
        barre = BarreRaccourcie.objects.all()
        name = 'Short an URL'
    return render(request, 'short.html', {
        'form': form,
        'barre': barre,
        'name': name
    })


def short_redirect(request, name):
    documents = Short.objects.get(name=name)
    return redirect(documents.url)


def short_sucessful(request, name):
    documents = Short.objects.get(name=name)
    barre = BarreRaccourcie.objects.all()
    name = 'Short an URL'
    return render(request, 'short_sucessful.html', {'documents' : documents, 'barre': barre, 'name': name})

def delete_url(request):
    documents = Short.objects.all()
    documents.delete()
    return redirect('short_url')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        mail = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        send_mail("De " +str(name)+"/"+str(mail)+" - "+str(subject),str(message)+"  De " +str(name)+"/"+str(mail), mail, ['emile.delmas@gmail.com'])
    barre = BarreRaccourcie.objects.all()
    name = 'Contact'
    return render(request, 'contact.html', {'barre': barre, 'contact': contact})

@login_required(login_url='/admin/')
def vekflix_index(request):
    films = Vekflix.objects.all()
    categories = []
    for film in films:
        if film.categorie not in categories:
            categories.append(film.categorie)
    return render(request, 'vekflix/index.html', {'films': films, 'categories': categories})

def vekflix_show(request, lien):
    film = Vekflix.objects.get(lien=lien)
    movies = Vekflix.objects.all()
    categories = []
    for movie in movies:
        if movie.categorie not in categories:
            categories.append(movie.categorie)
    return render(request, 'vekflix/show.html', {'movies': movies, 'categories': categories, 'film': film})

def file_vekflix(request, lien, type, file):
    stream = open('media/vekflix/' + str(type) +'/'+ str(file), 'rb')
    response = FileResponse(stream)
    return response

def ytb_vekflix(request):
    return render(request, 'vekflix/youtube.html')


def youtube_home(request):
    if request.method == 'POST':
        if request.POST.get('urlvideo',''):
            lien = request.POST.get('urlvideo','')
            yt = YouTube(lien)
            #os.system("youtube-dl -o media/youtube/%(title)s.%(ext)s -f best " + str(lien))
            yt.streams.first().download(output_path='media/youtube/')
            title = yt.streams.first().default_filename
           # return redirect('/media/youtube/'+title.replace(' ','%20')+'.mp4')
            file_path = FileWrapper(open('media/youtube/' + str(title), 'rb'))
            response = HttpResponse(file_path, content_type='video/mp4')
            response['Content-Disposition'] = 'attachment; filename=' + title
            return response
        elif request.POST.get('urlmusic',''):
            lien = request.POST.get('urlmusic','')
            yt = YouTube("https://www.youtube.com/" + str(lien))
            title = yt.title
            #os.system("youtube-dl -o media/youtube/%(title)s.%(ext)s -f bestaudio[ext=m4a] " + str(lien))
            yt.streams.filter(only_audio=True).first().download(output_path='media/youtube/')
            file_path = FileWrapper(open('media/youtube/' + str(title) + ".m4a", 'rb'))
            response = HttpResponse(file_path, content_type='audio/mp3')
            response['Content-Disposition'] = 'attachment; filename= "' + title.title() + '.mp3"'
            return response
    else:
        barre = BarreRaccourcie.objects.all()
        name = 'Youtube Downloader'
        return render(request, 'youtube.html', {'barre': barre, 'name': name})


def youtube_quality(request, lien):
    if request.GET.get('v',''):
        v = request.GET.get('v','')
        try:
            yt = YouTube("https://www.youtube.com/watch?v=" + str(v))
        except:
            NoReverseMatch
            return redirect('youtube',{'error': True})
    else:
        try:
            past = time.time()
            yt = YouTube("https://www.youtube.com/" + str(lien))
            now = time.time()
            delta = now-past
        except:
            NoReverseMatch
            return redirect('youtube',{'error': True})
    if request.method == 'POST':
        itag = request.POST.get("quality")
        if itag:
            title = yt.title
            lien = lien.replace("%3F", '?')
            link = "https://www.youtube.com/" + str(lien)
            os.system("youtube-dl -o media/youtube/%(title)s.%(ext)s -f best "+link)
            file_path = FileWrapper(open('media/youtube/'+str(title)+".mp4", 'rb'))
            response = HttpResponse(file_path, content_type='video/mp4')
            response['Content-Disposition'] = 'attachment; filename= "' + title.title() + '.mp4"'
            return response
    else:
        thumbnail = yt.thumbnail_url
        title = yt.title
        list = yt.streams.filter(subtype='mp4', type='video').order_by('resolution').desc().all()
        resolution = []
        fps = []
        itag = []
        for element in list:
            if str(element.resolution) not in resolution:
                resolution.append(str(element.resolution))
                fps.append(str(element.fps))
                itag.append(str(element.itag))
        barre = BarreRaccourcie.objects.all()
        name = 'Youtube Downloader'
        return render(request, 'youtube_quality.html', {
            'resolutions': resolution,
            'fps': fps,
            'itag': itag,
            'barre': barre,
            'name': name,
            'thumbnail': thumbnail,
            'title': title,
            })

@login_required()
def youtube_delete(request):
    folder = listdir('media/youtube')
    for file in folder:
        os.remove('media/youtube/'+str(file))
    return HttpResponse("<h1> All is clean :)</h1>")

def file_bus(request, file):
    stream = open('staticfiles/robert_bus/'+str(file), 'rb')
    response = FileResponse(stream)
    return response

def bus_home(request):
    if request.method == 'POST':
        stopA = request.POST.get('stopA')
        stopR = request.POST.get('stopR')
        return redirect('bus_link',stopA,stopR)
    else:
        return render(request, 'robert_bus.html',)

def bus_link(request, stopa, stopr):
    baseUrl = "https://traffic.api.iledefrance-mobilites.fr/v1/tr-vianavigo/departures?line_id=016096001%3A14&stop_point_id="
    apiKey = "810bbc8b4a96f25b28f1f45112762a585233e89c5f0eb9bb0bf1f580"
    stopA = stopa
    stopR = stopr
    if stopA == 'stopPoint:60:379':
        nameA = "GARE D'ENGHIEN-LES-BAINS"
    elif stopA == 'stopPoint:60:581':
        nameA = "GARE DE CHAMP DE COURSES D'ENGHIEN"
    elif stopA == 'stopPoint:60:598':
        nameA = "GENDARMERIE"
    elif stopA == 'stopPoint:60:575':
        nameA = "BONNE AUBERGE"
    elif stopA == 'stopPoint:60:634':
        nameA = "LES TOURELLES"
    elif stopA == 'stopPoint:60:342':
        nameA = "MONT D'EAUBONNE"
    elif stopA == 'stopPoint:60:334':
        nameA = "BOIS JACQUES"
    elif stopA == 'stopPoint:60:346':
        nameA = "TILLEULS"
    elif stopA == 'stopPoint:60:336':
        nameA = "HOTEL DE VILLE"
    elif stopA == 'stopPoint:60:338':
        nameA = "JEANNE D'ARC"
    elif stopA == 'stopPoint:60:344':
        nameA = "LA SABLIERE"
    elif stopA == 'stopPoint:60:340':
        nameA = "CHAUSSEE JULES CESAR"

    if stopR == 'stopPoint:60:1032':
        nameR = "GARE D'ERMONT EAUBONNE"
    elif stopR == 'stopPoint:60:581':
        nameR = "GARE DE CHAMP DE COURSES D'ENGHIEN"
    elif stopR == 'stopPoint:60:598':
        nameR = "GENDARMERIE"
    elif stopR == 'stopPoint:60:575':
        nameR = "BONNE AUBERGE"
    elif stopR == 'stopPoint:60:634':
        nameR = "LES TOURELLES"
    elif stopR == 'stopPoint:60:342':
        nameR = "MONT D'EAUBONNE"
    elif stopR == 'stopPoint:60:334':
        nameR = "BOIS JACQUES"
    elif stopR == 'stopPoint:60:346':
        nameR = "TILLEULS"
    elif stopR == 'stopPoint:60:336':
        nameR = "HOTEL DE VILLE"
    elif stopR == 'stopPoint:60:338':
        nameR = "JEANNE D'ARC"
    elif stopR == 'stopPoint:60:344':
        nameR = "LA SABLIERE"
    elif stopR == 'stopPoint:60:340':
        nameR = "CHAUSSEE JULES CESAR"
    url = baseUrl + stopA + "&apikey=" + apiKey
    resp = requests.get(url=url)
    data = resp.json()
    scheduleA = []
    i = 0
    while len(scheduleA) < 2:
        if data[i]['sens'] == 'A':
            scheduleA.append(i)
            i += 1
        else:
            i += 1
    nextStopA = data[scheduleA[0]]['time']
    nextnextStopA = data[scheduleA[1]]['time']
    url = baseUrl + stopR + "&apikey=" + apiKey
    resp = requests.get(url=url)
    data = resp.json()
    scheduleR = []
    i = 0
    while len(scheduleR) < 2:
        if data[i]['sens'] == 'R':
            scheduleR.append(i)
            i += 1
        else:
            i += 1
    nextStopR = data[scheduleR[0]]['time']
    nextnextStopR = data[scheduleR[1]]['time']
    return render(request, 'robert_bus_schedule.html', {'timeA': nextStopA, 'timeR': nextStopR, 'timenexta': nextnextStopA, 'timenextr': nextnextStopR, 'nameR': nameR, 'nameA': nameA})


def robert(request):
    return render(request, 'robert2.html')


def p5js(request):
    return render(request,'TPjs/index.html')

def exo(request,number):
    return render(request,'TPjs/exo.html',{'number':number})

def frac(request,string):
    string = urldecode(string)
    return render(request,'TPjs/'+string+'.html')


def qrcode(request):
    barre = BarreRaccourcie.objects.all()
    name = 'QR code'
    if request.method == 'POST':
        url = request.POST.get('url')
        return render(request,'qr.html',{'barre': barre,'url': url, 'name': name})
    else:
        return render(request,'qr.html',{'barre': barre,'name': name})

def steganography(request):
    barre = BarreRaccourcie.objects.all()
    name = 'stegano_encrypt'
    if request.method == 'POST':
        form = SteganoForm(request.POST, request.FILES)
        message = request.POST.get("message")
        key = request.POST.get("key")
        form.save()
        stegas = Stegano.objects.all()
        #picture = face[0]['picture']
        for stega in stegas:
            picture = stega.picture.name
        randomname = random.randint(1, 999999)
        picture = picture.split('/')[1]
        path = 'media/steganography/'+picture
        picture = 'media/steganography/results/Encrypt-'+str(randomname)+os.path.splitext(picture)[0]+'.png'
        im = Image.open(path)
        output = os.path.splitext(path)[0]+str(randomname)+'.png'
        im.convert('RGB').save(output,"PNG")
        crypto_steganography = CryptoSteganography(str(key))
        # Save the encrypted file inside the image
        crypto_steganography.hide(output, picture, str(message))
        secret = crypto_steganography.retrieve(picture)
        directory='media/steganography/'
        for file in os.scandir(directory):
            if file.name.endswith(".jpg"):
                os.unlink(file.path)
        stegas.delete()
        return render(request,'stegano.html',{'barre': barre,'name': name,'picture': picture,'secret':secret})
    else:
        steg = Stegano.objects.all()
        steg.delete()
        return render(request,'stegano.html',{'barre': barre,'name': name})

def steganographydecrypt(request):
    barre = BarreRaccourcie.objects.all()
    name = 'stegano_decrypt'
    if request.method == 'POST':
        form = SteganoForm(request.POST, request.FILES)
        key = request.POST.get("key")
        form.save()
        stegas = Stegano.objects.all()
        for stega in stegas:
            picture = stega.picture.name
        crypto_steganography = CryptoSteganography(str(key))
        randomname = random.randint(1, 999999)
        path = 'media/'+picture
        secret = crypto_steganography.retrieve(path)
        directory='media/steganography/'
        for file in os.scandir(directory):
            if file.name.endswith(".jpg"):
                os.unlink(file.path)
        stegas.delete()
        return render(request,'steganodecrypt.html',{'barre': barre,'name': name,'message': secret})
    else:
        return render(request,'steganodecrypt.html',{'barre': barre,'name': name})
    
def face_recognition(request):
    barre = BarreRaccourcie.objects.all()
    name = 'Face Recognition'
    if request.method == 'POST':
        form = FaceForm(request.POST, request.FILES)
        color = request.POST.get("color")
        color = color[1:]
        decolor = tuple(int(color[i:i+2], 16) for i in (4, 2, 0))
        #picture = request.FILES['picture'].name
        form.save()
        faces = FaceRecognition.objects.all()
        #picture = face[0]['picture']
        for face in faces:
            picture = face.picture.name
        randomname = random.randint(1, 999999)
        path = 'media/face_AI/'+picture.split('/')[1]
        im = Image.open(path)
        im.convert('RGB').save(os.path.splitext(path)[0]+str(randomname)+'.jpg',"JPEG")
        imagePath = 'media/'+os.path.splitext(picture)[0]+str(randomname)+'.jpg'
        cascadeClassifierPath = "media/haarcascade_frontalface_alt.xml"
        cascadeClassifier = cv2.CascadeClassifier(cascadeClassifierPath)
        image = cv2.imread(imagePath)
        grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        detectedFaces = cascadeClassifier.detectMultiScale(grayImage)
        for (x,y,width,height) in detectedFaces:
            cv2.rectangle(image, (x,y), (x+width, y+height),decolor,5)
        picture = 'FaceR-'+str(randomname)+picture.split('/')[1]
        cv2.imwrite('media/face_AI/results/'+picture, image)
        directory='media/face_AI/'
        for file in os.scandir(directory):
            if file.name.endswith(".png") or file.name.endswith(".jpg"):
                os.unlink(file.path)
        faces.delete()
        return render(request,'face_recognition.html',{'barre': barre,'name': name,'picture':picture})
    else:
        faces = FaceRecognition.objects.all()
        faces.delete()
        faceform = FaceForm()
        return render(request,'face_recognition.html',{'barre': barre,'name': name,'faceform':faceform})


def translate(request):
    barre = BarreRaccourcie.objects.all()
    name="translation"
    if request.method == "POST":
        orginal_text = request.POST.get("orginal_text")
        splitText = orginal_text.split("\r\n")

        t = Translator("EN", "FR")
        translatedText = []
        for text in splitText:
            translatedText.append(t.translate_sentences(text))
        return render(request,'translate.html',{'barre':barre,'name':name,'translatedText':translatedText})
    else:
        return render(request,'translate.html',{'barre':barre,'name':name})
    
    
def random_person(request):
    barre = BarreRaccourcie.objects.all()
    name="Face Generation"
    if request.method == 'POST':
        number = int(request.POST.get("number"))
        picturesArray = []
        picturesCheksum = []
        i = 0
        mypath = 'media/doesnotexist/'
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        while i<number:
            if i<10:
                picture = get_online_person()  # bytes representation of the image
                checksum2 = get_checksum_from_picture(picture)  # Method is optional, defaults to "md5"
                if checksum2 not in picturesCheksum:
                    randomname = random.randint(100000000, 999999999)
                    path = "media/doesnotexist/Random_Person_"+str(randomname)+".jpeg"
                    save_picture(picture, path)
                    picturesArray.append(path)
                    picturesCheksum.append(checksum2)
                    i+=1
            else:
                listnb = random.randint(0, len(onlyfiles)-1)
                if "media/doesnotexist/"+onlyfiles[listnb] not in picturesArray:
                    picturesArray.append("media/doesnotexist/"+onlyfiles[listnb])
                    i+=1
        return render(request,'random_person.html',{'picturesArray':picturesArray,'barre':barre,'name':name,'number':number})
    else:
        number = 10
        return render(request,'random_person.html',{'barre':barre,'name':name,'number':number})


def sendmail(request,matiere,note):
    send_mail("Nouvelle note ",matiere+" : "+note,"test@gmail.com", ['emile.delmas@gmail.com'])
    return render(request,'sendmail.html')

def mathtraining(request):
    barre = BarreRaccourcie.objects.all()
    name="Bac Maths"
    exercices = Exercice.objects.all()
    chapitres = []
    total = exercices.count()
    for ex in exercices:
        liste = ex.chapitres.split('\n')
        for chapitre in liste:
            if chapitre.replace('\r','') not in chapitres:
                chapitres.append(chapitre.replace('\r',''))
    if request.method == 'POST':
        time = request.POST.get("time")
        number = request.POST.get("number")
        types = request.POST.get("type")
        number_selected = []
        chapitres_selected = []
        chapitres_not_selected = []
        for chapitre in chapitres:
            number_selected.append(request.POST.get(chapitre, '') == 'on')
        
        for i in range(0,len(chapitres)):
            if number_selected[i]==True:
                chapitres_selected.append(chapitres[i])
            else:
                chapitres_not_selected.append(chapitres[i])
        ex = exercices
        #for chapitre in chapitres_selected:
        #exercices = exercices.filter(chapitres__in=chapitres_selected)
        queries = [Q(chapitres__icontains=chapitre) for chapitre in chapitres_selected]
        # Take one Q object from the list
        query = queries.pop()
        # Or the Q object with the ones remaining in the list
        for item in queries:
            query |= item
        exercices = exercices.filter(query)
        for chapitre in chapitres_not_selected:
            exercices = exercices.exclude(chapitres__icontains=chapitre)
        exercices = exercices.order_by('?')
        old_exercices = exercices

        if types == "time":
            total_time = int(time)
            exclude_pk = []
            for exercice in old_exercices:
                tim = int(exercice.points)*10
                if int(exercice.points)*10 <= total_time:
                    total_time = total_time - int(exercice.points)*10
                else:
                    exclude_pk.append(exercice.pk)
            exercices = exercices.exclude(pk__in=exclude_pk)
            total_time = 0
            for exercice in exercices:
                total_time += int(exercice.points)*10
            hour = math.floor(total_time/60)
            minutes = total_time-hour*60
        else:
            include_pk = []
            exclude_pk = []
            i = 0
            for exercice in exercices:
                if i<int(number):
                    include_pk.append(exercice.pk)
                i+=1
            for exercice in exercices:
                if exercice.pk not in include_pk:
                    exclude_pk.append(exercice.pk)
            exercices = exercices.exclude(pk__in=exclude_pk)
            hour = "illimité"
            minutes = 0
        seriesChapitres = []
        for ex in exercices:
            liste = ex.chapitres.split('\n')
            for chapitre in liste:
                if chapitre.replace('\r','') not in seriesChapitres:
                    seriesChapitres.append(chapitre.replace('\r',''))
        number = exercices.count()
        return render(request,'exercice_math.html',{'exercices':exercices,'hour':hour,'minutes':minutes,'seriesChapitres':seriesChapitres,'chapitres':chapitres_selected,'number':number,'barre':barre,'name':name})
    else:
        number = 120
        return render(request,'trainingmath.html',{'number':number,'exercices':exercices,'chapitres':chapitres,'barre':barre,'name':name,'total':total})
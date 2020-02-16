from django.db import models
from colorfield.fields import ColorField
import locale

class BarreRaccourcie(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    logo = models.CharField(max_length=100, blank=True, null=True)


class UploadPassword(models.Model):
    password = models.CharField(max_length=100)

class Projet(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    language = models.CharField(max_length=10, help_text='Entrer le langage majoritairement utilisé dans votre projet')
    git = models.URLField(help_text='Entrer le lien de votre page Github ou Gitlab', blank=True)
    site = models.URLField(help_text='Entrer le lien du site du projet', blank=True)
    article = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    font_size = models.IntegerField()


    def __str__(self):
        return self.title

    def body_preview(self):
        return self.body[:50]


class Document(models.Model):
    folder = models.CharField(max_length=100)
    file = models.FileField(upload_to='uploads/')
    password = models.CharField(max_length=100, null=True, blank=True, help_text="Mot de passe facultatif demandé à l'ouverture du fichier")
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Short(models.Model):
    url = models.CharField(max_length=200)
    name = models.CharField(max_length=100)


class Vekflix(models.Model):
    title = models.CharField(max_length=100)
    lien = models.CharField(max_length=100)
    categorie = models.CharField(max_length=20, null=True, blank=True)
    description = models.CharField(max_length=100)
    simple_description = models.CharField(max_length=20)
    film = models.FileField(upload_to='vekflix/film/')
    youtube_link = models.CharField(max_length=200, null=True, blank=True)
    realisator = models.CharField(max_length=20, null=True, blank=True)
    main_actor = models.CharField(max_length=20, null=True, blank=True)
    jacket = models.ImageField(upload_to='vekflix/image/', help_text="Format 150px/250px ")
    mignature = models.ImageField(upload_to='vekflix/image/',help_text="Format 16/9")


class Youtube(models.Model):
    url = models.CharField(max_length=200)


class Stegano(models.Model):
    message = models.CharField(max_length=500)
    picture = models.ImageField(upload_to='steganography/')
    key = models.CharField(max_length=100)

class FaceRecognition(models.Model):
    picture = models.ImageField(upload_to='face_AI/')   


class Exercice(models.Model):
    sujet = models.FileField(upload_to='uploads/trainingmath/sujets/')
    correction = models.FileField(upload_to='uploads/trainingmath/corrections/')
    chapitres = models.TextField()
    annee = models.CharField(max_length=10)
    points = models.CharField(max_length=10)
    difficulte = models.CharField(max_length=30)
    def chapitres_as_list(self):
        return self.chapitres.split('\n')
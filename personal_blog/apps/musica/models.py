import os
from django.db import models
from mutagen.easyid3 import EasyID3
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Autor(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
        
class Album(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Autor,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
class Genero(models.Model):
    name =models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

def get_file_path(instance, filename):
    filename=instance.name 
    return "music/{0}.mp3".format(filename)

class Musica(models.Model):
    fileMusic = models.FileField(upload_to=get_file_path)
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Autor, on_delete=models.CASCADE,related_name='author_related')
    colaborators = models.ManyToManyField(Autor,blank=True,related_name='colaborators_set')
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    track_number = models.IntegerField(blank=True)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    url = models.URLField(blank=True)
    letra = models.TextField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


@receiver(post_save, sender=Musica)
def change_etiquetas(sender,instance,created,**kwargs):
    if created:
        file_name = str(instance.fileMusic).split('/')[1]
        path_file = os.path.join("./media/music",file_name)
        audio = EasyID3(path_file)
        audio["album"]=[str(instance.album)]
        audio["title"]=[str(instance.name)]
        audio["artist"]=[str(instance.author)]
        audio["tracknumber"]=[str(instance.track_number)]
        audio["genre"]=[str(instance.genero)]
        audio.save()
    




from django.contrib import admin
from .models import Autor,Album,Genero,Musica
# Register your models here.

admin.site.register(Autor)
admin.site.register(Genero)
admin.site.register(Album)
admin.site.register(Musica)
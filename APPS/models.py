from ckeditor.fields import RichTextField
from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
class Post(models.Model):
    autor = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    resumo = RichTextField(blank=True, null=True)
    conteudo = RichTextUploadingField()
    imagem_capa = models.ImageField(blank=True, null=True, upload_to='static/APPS/')
    data_publicacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo



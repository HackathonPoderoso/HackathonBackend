from django.db import models
from uploader.models import Image

class Teste(models.Model):
    texto = models.CharField(max_length=50, null=True, blank=True)
    imagem = models.ForeignKey(Image, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.texto

    class Meta:
        verbose_name = "Teste"
        verbose_name_plural = "Testes"
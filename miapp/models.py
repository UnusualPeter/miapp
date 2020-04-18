from django.db import models

# Create your models here.
class Notas(models.Model):
    texto = models.CharField(max_length=200)
    pub_date = models.DateTimeField('fecha de publicación')

    def __str__(self):
        return '{}'.format(self.texto)

    class Meta:
        verbose_name_plural = 'Notas'
from django.db import models

# Create your models here.

class Pencarian_Keyword(models.Model):
    url = models.CharField(max_length = 100)
    keyword = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.url

class Hasil_Pencarian_Keyword(models.Model):
    word_result = models.CharField(max_length = 1000)
    
    def __str__(self):
        return self.word_result
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


# Create your models here.

# elektron kutubxona formasi

class Bolim(models.Model):  # bo'limlarni kiritish uchun forma  (faqat admin uchun)
    bolim = models.CharField("Bo'lim", max_length=255)

    def __str__(self):
        return self.bolim


class Til(models.Model):  # tilni kiritish uchun forma   (faqat admin uchun)
    til = models.CharField(max_length=100)

    def __str__(self):
        return self.til


class KitobShakli(models.Model):  # kitob shaklini kiritish uchun forma (faqat admin)
    kitob_shakli = models.CharField(max_length=120)

    def __str__(self):
        return self.kitob_shakli


class Form(models.Model):  # foydalanuvchi kiritish uchun forma
    kitob_nomi = models.CharField(max_length=500)
    kitob_muqovasi = models.ImageField(upload_to='images')
    kitob_fayli = models.FileField(upload_to='uploads/%Y/%m/%d/')
    muallif = models.CharField(max_length=200)
    bolim = models.ForeignKey(Bolim, on_delete=models.CASCADE, blank=True, null=True)
    ishlab_chiqaruvchi = models.CharField(max_length=200)
    til = models.ForeignKey(Til, on_delete=models.CASCADE)
    seriya = models.CharField(max_length=370)
    yil = models.IntegerField()
    bet = models.IntegerField()
    kitob_haqida = RichTextField()
    isbn = models.CharField(max_length=400)
    kitob_shakli = models.ForeignKey(KitobShakli, on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, )
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.kitob_nomi

    def get_absolute_url(self):  # new
        return reverse('form_detail', args=[str(self.id)])


# ==========COMMENTS

class Comment(models.Model):  # kitoblar uchun comment
    post = models.ForeignKey(Form, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    comment = models.TextField(max_length=400)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.comment[:60]


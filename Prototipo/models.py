from django.db import models
from django.utils import timezone


class Post(models.Model):
        author = models.ForeignKey('auth.User')
        title = models.CharField(max_length=200)
        text = models.TextField()
        created_date = models.DateTimeField(
                default=timezone.now)
        published_date = models.DateTimeField(
                blank=True, null=True)

        def publish(self):
            self.published_date = timezone.now()
            self.save()

        def __str__(self):
            return self.title


class Sismo(models.Model):
        author = models.ForeignKey('auth.User')
        title = models.CharField(max_length=200)
        text = models.TextField()
        eje_x = models.FileField(upload_to='myfolder/', blank=True)
        eje_y = models.FileField(upload_to='myfolder/', blank=True)
        eje_z = models.FileField(upload_to='myfolder/', blank=True)
        network = models.CharField(max_length=200)
        station = models.CharField(max_length=200)
        channel = models.CharField(max_length=200)
        starttime = models.CharField(max_length=200)
        endtime = models.CharField(max_length=200)
        sampling_rate = models.CharField(max_length=200)
        delta = models.CharField(max_length=200)
        npts= models.CharField(max_length=200)
        calib = models.CharField(max_length=200)
        format = models.CharField(max_length=200)
        created_date = models.DateTimeField(
            default=timezone.now)
        published_date = models.DateTimeField(
            blank=True, null=True)

        def publish(self):
            self.published_date = timezone.now()
            self.save()

        def __str__(self):
            return self.title
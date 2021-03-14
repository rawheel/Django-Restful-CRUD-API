from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    city = models.CharField(max_length=10)
    zipcode = models.CharField(max_length=10)
    other  = models.CharField(max_length=50)
    start_date = models.CharField(max_length=25)
    end_date = models.CharField(max_length=25)
    category = models.CharField(max_length=25)
    list_date = models.DateTimeField(auto_now=True,blank = True)
    class Meta:
        verbose_name_plural = 'events'
    def __str__(self):
        return self.title

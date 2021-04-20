from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    community = models.CharField(max_length=15,default=None)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    date = models.DateField()
    time = models.TimeField(default=None)
    category = models.CharField(max_length=25)
    MODE_CHOICES=[
        ('phy',"Physical"),
        ('on',"Online")
    ]
    mode=models.CharField(choices=MODE_CHOICES,max_length=3)
    date_created = models.DateTimeField(auto_now=True,blank = True)

    class Meta:
        verbose_name_plural = 'events'
    def __str__(self):
        return self.title

from django.db import models


# Create your models here.

class eventDetail(models.Model):
    id = models.CharField(max_length=15,primary_key=True)
    realName = models.CharField(max_length=50,default="")
    timeZone = models.CharField(max_length=50,default="")


class eventTime(models.Model):
    id = models.AutoField(primary_key=True)
    eventDetail = models.ForeignKey(eventDetail, on_delete=models.CASCADE,default=None)
    startTime = models.CharField(max_length=30,default="")
    endTime = models.CharField(max_length=30,default="")



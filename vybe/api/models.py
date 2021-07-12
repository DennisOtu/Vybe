from django.db import models
import random
import string

def generateUniqueCode():
    length = 6
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if room.objects.filter(code=code).count() == 0:
            break
    return code
        
class Room(models.Model):
    code = models.CharField(max_length=8, default='', unique=True)
    host = models.CharField(max_length=50, unique=True)
    guestCanPause = models.BooleanField(null=False, default=False)
    votesToSkip = models.IntegerField(null=False, default=1)
    createdOn = models.DateTimeField(auto_now_add=True)


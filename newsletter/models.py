from django.db import models

# Create your models here.
STATUS_CHOICES = (
    ('c', 'czeka na akceptacje'),
    ('a', 'zaakceptowany'),
    ('n', 'niezaakceptowany')
)

class SignUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=120, null=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=True, auto_now=False)
    status = models.CharField(max_length=1, choices = STATUS_CHOICES)
    prezentacja = models.CharField(max_length=360, null=False)


    def __unicode__(self): #Python 3.3 is __str__
        return self.email


# class Czlonkowie(models.Model):
#     czlonek = models.ForeignKey( SignUp )
#     email = models.EmailField( SignUp )
#     full_name = models.CharField( SignUp, max_length=120)
#
#     def __unicode__(self):
#         return self.czlonek.email

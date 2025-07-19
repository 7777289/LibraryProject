from django.db import models



class Book(models.Model):

&nbsp;   title = models.CharField(max\_length=200)

&nbsp;   author = models.CharField(max\_length=100)

&nbsp;   publication\_year = models.IntegerField()



&nbsp;   def \_\_str\_\_(self):

&nbsp;       return self.title




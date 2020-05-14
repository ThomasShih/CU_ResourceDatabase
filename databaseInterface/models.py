from django.db import models

class Chapter(models.Model):
  subject = models.CharField(max_length=4)
  title   = models.CharField(max_length=100)
  fileName= models.CharField(max_length=103)

  def __str__(self):
      return "{}: {}".format(self.subject,self.title)

class Course(models.Model):
  subject = models.CharField(max_length=4)
  code    = models.PositiveSmallIntegerField()
  descFile= models.CharField(max_length=11)
  chapters = models.ManyToManyField(Chapter)

  def __str__(self):
      return self.subject + str(self.code)
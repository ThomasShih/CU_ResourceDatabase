from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers

from .models import Chapter,Course

markdownFilePath = ".\\markdownFiles\\"

retrieveError404 = {
  "status":404,
  "message":"Could not retrieve",
}

def getChapterMD(request=None,key=None,inputfileName=None):
  """Returns markdown file of selected chapters"""
  fileName = Chapter.objects.get(pk=key).fileName if inputfileName == None else inputfileName
  filePath = markdownFilePath + fileName
  with open(filePath,"r") as file: markdown = file.read()
  return JsonResponse({"markdownString":markdown}) if inputfileName == None else markdown

def availableCourses(request):
  """Returns the list of currently available courses"""
  try:
    courseList = Course.objects.all()
    response = [{"subject":c.subject,"code":c.code} for c in courseList]
    return JsonResponse(response,safe=False)
  except: return JsonResponse(retrieveError404,status=404)

def getChapter(key):
  chapter = Chapter.objects.get(pk=key)
  return {
    "title":chapter.title,
    "primaryKey":chapter.id,
  }

def getCourse(request,subject,code):
  """Returns the detailed information of the selected course"""
  try:
    course = Course.objects.get(subject=subject,code=code)
    response = {
      "subject":course.subject,
      "code":course.code,
      "desc":getChapterMD(inputfileName=course.descFile),
      "chapters":[getChapter(chapter.id) for chapter in course.chapters.all()],
    }
    return JsonResponse(response)
  except: return JsonResponse(retrieveError404,status=404)
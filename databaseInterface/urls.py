from django.urls import path

from . import views

urlpatterns = [
  path('', views.availableCourses),
  path('course/<str:subject>/<int:code>/',views.getCourse),
  path('md/<int:key>/',views.getChapterMD),
]
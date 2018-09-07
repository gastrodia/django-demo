from django.conf.urls import url
from . import views
from .views import Student
urlpatterns =[
     url(r'^student/$', Student.as_view(),name='student')
]
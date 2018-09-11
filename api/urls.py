from django.conf.urls import url, include
from api import views

urlpatterns = [
    url(r'^', include(views.router.urls)),
    url(r'^runJob/$',views.run_job),
]
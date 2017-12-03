from django.conf.urls import url
from start import views

urlpatterns = [

    url(r'^', views.Index.as_view()),

]

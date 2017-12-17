from django.conf.urls import url

from newspaper import views

urlpatterns = [
    url(r'^$',views.index ,name="index"),
    url(r'^signups/$',views.signups ,name="signups"),
    #url(r'^/$'),
    #url(r'^(?P<>[0-9]+)/$'),    
]

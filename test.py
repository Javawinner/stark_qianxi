from django.conf.urls import url
from app01 import views as v1
from app02 import views as v2

class Stark(object):
    def __init__(self):
        self.register = []

    @property

    def get_urls(self):
        urlpatterns=[]
        for app in self.register:
            if app=='app01':
                urlpatterns.append(url(r'^%s/'%app, v1.index))
            if app=='app02':
                urlpatterns.append(url(r'^%s/' % app, v2.index))
        return (urlpatterns,None,None)


site=Stark()

"""scratchQsDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
# from scratchQs import views
from scratchQs import views as scratchq_views

urlpatterns = [
    url(r'^scratchQs/admin/', admin.site.urls),
    #url(r'^scratchQs/$', scratchq_views.index, name="index"),
    url(r'^scratchQs/questions/', scratchq_views.IndexView.as_view(), name="index"),
    #url(r'^scratchQs/questions/', scratchq_views.index, name="index"),
    url(r'^scratchQs/(?P<question_id>[0-9]+)/$', scratchq_views.answers, name="answers"),
    url(r'^scratchQs/community/(?P<community_id>[0-9]+)/$', scratchq_views.community_questions, name="community_questions"),
    url(r'^scratchQs/signup', scratchq_views.signup, name="signup"),
    #url(r'^scratchQs/answer/$', scratchq_views.answer_page, name="answer_page") #not working yet
]

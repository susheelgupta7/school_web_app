from django.conf.urls import url
from Mobile_app import views
from django.urls import path
app_name='Mobile_app'
urlpatterns = [
    url(r'^result/$',views.result,name='result'),
    url(r'^about/$',views.about,name='about'),
    url(r'^blog/$',views.blog,name='blog'),
    path('contact/',views.contact,name='contact'),
    url(r'^teacher/$',views.teacher,name='teacher'),
    url(r'^courses/$',views.courses,name='courses'),
    url(r'^activities/$',views.activities,name='activities'),
    url(r'^createcourse/$',views.createcourse,name='createcourse'),
    url(r'^subjects/$',views.subjects,name='subjects'),
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]

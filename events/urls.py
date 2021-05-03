from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    #path('events/',views.EventList.as_view()),
    path('events/', views.EventList.as_view()),
    path('events/<int:pk>/', views.EventDetails.as_view()),
    #path('eventdel/<int:pk>/', views.EventDel.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
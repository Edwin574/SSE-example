from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path("stream-data/", views.sse_stream, name='stream_data'),
]
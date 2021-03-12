from django.urls import path
from .views import HomepageView,CvpageView

app_name='portfolio'

urlpatterns= [
    path('',HomepageView.as_view(),name='homepage'),
    path('cv/',CvpageView.as_view(),name='cv'),
]

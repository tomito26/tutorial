from django.urls import path
from .views import ListTutorialView

urlpatterns = [
    path('tutorials/',ListTutorialView.as_view(), name='tutorial-all')
]
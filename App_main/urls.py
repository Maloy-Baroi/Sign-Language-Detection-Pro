from django.urls import path
from App_main.views import *

app_name = 'App_main'


urlpatterns = [
    path('', home, name='home'),
    path('hand-detection', hand_detection, name='hand-detection'),
    path('sign-to-text/', sign_to_text, name='sign-to-text'),
    path('speech-to-sign/', speech_to_sign, name='speech-to-sign'),
    path('about-us', about_us, name='about-us'),
    path('project-documentation/', project_documentation, name='project-documentation'),
]


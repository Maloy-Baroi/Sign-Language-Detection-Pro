from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return redirect('/sign-to-text/')
    # return redirect('App_main:sign-to-text')


def hand_detection(request):
    return render(request, 'App_main/hand_detector.html')


def speech_to_sign(request):
    return render(request, 'App_main/speech_to_sign.html')


def sign_to_text(request):
    myModel = open("App_main/model/signModel.h5", "r")
    content = {
        'myModel': myModel,
    }
    return render(request, 'App_main/sign_to_text.html', context=content)


def about_us(request):
    return render(request, 'App_main/about_us.html')


def project_documentation(request):
    return render(request, 'App_main/project_documentation.html')


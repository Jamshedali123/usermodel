from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from app.forms import *

from django.core.mail import send_mail

 
def registration(request):
    USFO=Userform()
    PFO=ProfileForm()
    d={'USFO':USFO,'PFO':PFO}



    if request.method=='POST' and request.FILES:
        UFDO=Userform(request.POST)
        PFDO=ProfileForm(request.POST,request.FILES)

        if UFDO.is_valid() and PFDO.is_valid():
            MUFDO=UFDO.save(commit=False)
            MUFDO.set_password(UFDO.cleaned_data['password'])
            MUFDO.save()

            MPFDO=PFDO.save(commit=False)
            MPFDO.username=MUFDO
            MPFDO.save()

            send_mail('registration',
                      'helloo---->>>today is your opportunity to build the tomarrow you want::>>JAMSHED ALI',
                      'ajamshed456@gmail.com',
                      [MUFDO.email],
                      fail_silently=False
                      )
            
            return HttpResponse('Registration is successfull')

    return render(request,'registration.html',d)

from django.shortcuts import redirect, render
from .models import Details,Finder,Register
from django.contrib import messages
import random
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings

# Create your views here.



def index(request):
    print("start")
    if 'random_object' in request.session:
            del request.session['random_object']
             
            del request.session['email'] 
            
            request.session.save()
    

    return render(request,"index.html")

def register(request):
    print("start")

    if request.method == "POST":
        
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        birthdayDate = request.POST.get('birthdayDate')
        gender = request.POST.get('inlineRadioOptions')
        email = request.POST.get('emailAddress')
        phoneNumber = request.POST.get('phoneNumber')
        username = request.POST.get('username')
        url = request.POST.get('url')
        other = request.POST.get('other')

        person=Register(f_name=firstName,
                 l_name=lastName,
                 birthdate=birthdayDate,
                 email=email,
                 phone=phoneNumber,
                 u_name=username,
                 link=url,
                 other=other,
                 gender=gender)
        person.save()


        # request.session['firstName'] = firstName
        # request.session['lastName'] = lastName
        # request.session['birthdayDate'] = birthdayDate
        # request.session['gender'] = gender
        # request.session['email'] = email
        # request.session['phoneNumber'] = phoneNumber
        # request.session['username'] = username
        # request.session['url'] = url
        # request.session['other'] = other
        # request.session.save()
        
        
        msge=" has been successfully updated"
        messages.info(request, msge)      
    return render(request,"register.html")

def friend_find(request):
    if request.method == "POST":
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        birthdayDate = request.POST.get('birthdayDate')
        gender = request.POST.get('inlineRadioOptions')
        email = request.POST.get('emailAddress')
        phoneNumber = request.POST.get('phoneNumber')


        all_ids = Register.objects.values_list('id', flat=True)
        random_id = random.choice(all_ids)
        random_object = Register.objects.get(id=random_id)
        request.session['random_object'] = random_object
        request.session['email'] = email
        request.session.save()

        savedetails=Details(f_f_name=firstName,f_l_name=lastName,f_birthdate=birthdayDate,f_email=email,f_phone=phoneNumber,f_gender=gender,
                            mate_f_name=random_object.f_name,
                            mate_l_name=random_object.l_name,
                            mate_birthdate=random_object.birthdate,
                            mate_email=random_object.email,
                            mate_phone=random_object.phone,
                            mate_u_name=random_object.u_name,
                            mate_link=random_object.link,
                            mate_other=random_object.other,
                            meta_gender=random_object.gender)
        savedetails.save()

        

        
    return render(request,"find_pay.html")

def send_details(request):


    
    # if 'random_object' in request.session:
    #     del request.session['random_object']
        
    #     request.session.save()

    if 'random_object' in request.session:
        mate=request.session['random_object']
        finder=request.session['email'] 

        email_subject="Mate Details"
        message=render_to_string('payment_sucess_mail.html',{
        
            'mate_f_name':mate.f_name,
            'mate_l_name':mate.l_name,
            'mate_birthdate':mate.birthdate,
            'mate_email':mate.email,
            'mate_phone':mate.phone,
            'mate_u_name':mate.u_name,
            'mate_link':mate.link,
            'mate_other':mate.other,
            'meta_gender':mate.gender,
        
        

        })
        print("mail attemptting")
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [finder]

        email_message = EmailMessage(email_subject,message,email_from,recipient_list)
        
        email_message.content_subtype = "html"
        email_message.send()
        
        
    return redirect('index')
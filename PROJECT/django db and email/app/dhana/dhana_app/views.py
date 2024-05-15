from django.shortcuts import render
from.models import uv
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render(request,"index.html")
def redi(request):
    name=request.POST.get("name")
    mail=request.POST.get("mail")
    d={"name":name,"mail":mail}
    # send_mail(
    # "Subject here",
    # "Here is the message.",
    # "dhanakk005@gmail.com",
    # [mail],
    # fail_silently=False,

    subject = 'welcome to GFG world'
    message = f'Hi {name}, thank you for registering in geeksforgeeks.'
    email_from = 'dhanakk005@gmail.com'
    recipient_list = [mail]
    send_mail( subject, message, email_from, recipient_list )


    a=uv(name=name,mail=mail)
    a.save()
    return render(request,"redirect.html",d)

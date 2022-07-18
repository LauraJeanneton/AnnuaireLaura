from django.shortcuts import render
from repertoire.models import Contact

def home(request):
    nb_users = Contact.objects.all().count()
    all_users = Contact.objects.all()
    expiration_date = request.session.get_expiry_date()
    context = {
        'nb_users' : nb_users,
        'all_users' : all_users,
        'expiration_date':expiration_date
    }
    return render(request,'home.html',context=context)

def details(request, idUser):
    user = Contact.objects.get(id=idUser)
    context = {
        'user' : user,

    }
    return render(request,'details.html',context=context)

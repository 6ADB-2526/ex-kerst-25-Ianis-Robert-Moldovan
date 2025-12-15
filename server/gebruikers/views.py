from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from gebruikers.models import GebruikersLogin
from django.forms.models import model_to_dict
import json


# Create your views here.

# hier maak ik een functie die all je users
# terug zal geven in je browser met JSON
def alleUsers(request):
    users = GebruikersLogin.objects.alL()
    return JsonResponse(users)

# get 1 user
def oneUser(request):
    user = GebruikersLogin.objects.get(id = id)
    




# hier maak ik een nieuwe user aan 
# door gebruik van post_data zodat ik gegevens mee kan sturen 
# met postman
@csrf_exempt
def addUser(request):
    post_data =  json.loads(request.body.decode('utf-8'))
    new_user = post_data
    new_user.login = post_data["login"],
    new_user.password = post_data["password"],
    new_user.email = post_data["email"],
    new_user.role = post_data["role"],
    new_user.superUser = post_data["superUser"]
    new_user.save()
    return JsonResponse(model_to_dict(addUser))
    

# hier maak ik een function die een user verwijderd op basis van 
# het gekozen id
def deleteUser(request,id):
    user = GebruikersLogin.objects.get(id = id)
    user.delete()
    return JsonResponse(deleteUser)


# def updateUser(request):


# aanmelden 
# wachtwoord aanpassen
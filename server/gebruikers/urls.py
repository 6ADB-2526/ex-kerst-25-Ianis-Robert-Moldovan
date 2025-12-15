from django.urls import path

from . import views


# hier heb ik mijn urls gemaakt die je nodig hebt voor het web
# zoals allUsers/ die verbonden is aan de functie alleUsers 
# en zo heb ik het gedaan met alle andere functies en paths / urls
urlpatterns = [
    path('allUsers/', views.alleUsers),
    path('oneUser/', views.oneUser),
    path('addUser/', views.addUser),
    path('deleteUser/<int:id>', views.deleteUser),
    path('updateUser/<int:id>', views.updateUser),
]
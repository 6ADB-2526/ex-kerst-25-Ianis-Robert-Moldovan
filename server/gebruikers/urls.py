from django.urls import path

from . import views

urlpatterns = [
    path('allUsers/', views.alleUsers),
    path('oneUser/', views.oneUser),
    path('addUser/', views.addUser),
    path('deleteUser/<int:id>', views.deleteUser),
    path('updateUser/<int:id>', views.updateUser),
]
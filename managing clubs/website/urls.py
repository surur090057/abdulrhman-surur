from django.urls import path 
from . import views
urlpatterns = [
    path('',views.home, name='home'),
   # path('login/',views.loginUser, name='home'),
    path('logout/',views.logoutUser, name='logout'),
    path('register/',views.registerUser, name='register'),
    path('AddPlayer/',views.AddPlayer, name='AddPlayer'),
    path('player_info/',views.playerInfo, name='player_info'),
    path('delete/<int:pk>/<str:tableName>/<str:columnName>/',views.delete, name='delete'),
    path('updatePl/<int:pk>',views.updatePl, name='updatePl'),
    path('updateInfo/<int:pk>',views.updateInfo, name='updateInfo'),
    path('clubs/',views.clubs, name='clubs'),
    path('addInfos/',views.addInfos, name='addInfos'),
    path('updateClub/<int:pk>',views.updateClub, name='updateClub'),
    path('addClub/',views.addClub, name='addClub'),
    path('coach/',views.coach, name='coach'),
    path('updateCoach/<int:pk>',views.updateCoach, name='updateCoach'),
    path('addCoach/',views.addCoach, name='addCoach'),
    path('worker/',views.worker, name='worker'),
    path('addWorker/',views.addWorker, name='addWorker'),
    path('updateWorker/<int:pk>',views.updateWorker, name='updateWorker'),
    path('category/',views.category, name='category'),
    path('addCategory/',views.addCategory, name='addCategory'),
    path('updateCategory/<int:pk>',views.updateCategory, name='updateCategory'),
    path('contract/',views.contract, name='contract'),
    path('updateContract/<int:pk>',views.updateContract, name='updateContract'),
    path('addContract/',views.addContract, name='addContract'),






    












    

]

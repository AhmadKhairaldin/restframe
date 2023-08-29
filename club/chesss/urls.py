from django.urls import path,include
from . import views
urlpatterns =[
    path('',views.getclub,name='getclub'),
    path('addclub',views.addclub,name='adddata-club'),
    # fortourment
    path('gettour',views.getdata,name='datatourment'),
    path('addtour',views.insertdata,name='adddata'),
    path('updatetour/<int:id>/',views.updatedata,name='upatedata'),
    path('deletetour/<int:id>',views.detetedata,name='deletedata'),
    # for member
    path('addmem',views.addmem,name='addmem'),
    path('getmem',views.getmem,name='getmem'),
    path('updatemem/<int:id>/',views.updatemem,name='upatemem'),
    path('deletemem/<int:id>',views.detetemem,name='deletemem'),
    # for player
    path('addplay',views.insertplay,name='addplay'),
    path('getplay',views.getplay,name='getplay'),
    path('updateplay/<int:id>/',views.updateplay,name='upateplay'),
    path('deleteplay/<int:id>',views.deteteplay,name='deleteplay'),
    #  for match
    path('addmat',views.insertmatch,name='addmat'),
    path('getmat',views.getmatch,name='getmat'),
    path('updatemat/<int:id>/',views.updatematach,name='upatemat'),
    path('deletemat/<int:id>',views.detetemacth,name='deletemat'),

]
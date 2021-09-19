from django.urls import path
from .views import Addlaptopview, Deletelaptopview, Homeview,Showlaptopview, Updatelaptopview, listing


urlpatterns=[
    path('addlaptop/',Addlaptopview,name='addlaptop'),
    path('showlaptop/',Showlaptopview,name='showlaptop'),
    path('updatelaptop/<int:update>',Updatelaptopview,name='updatelaptop'),
    path('deletelaptop/<int:delete>',Deletelaptopview,name='deletelaptop'),
    path('listing/',listing.as_view(),name='listing'),
    path('home/',Homeview,name='home')
]
from  django.urls import path 
from .views import contact_us, home_page, about_us 



urlpatterns = [
    path('home/',home_page,name ='home'),
    path('contact_us/',contact_us,name ='contact'),
    path('about_us/',about_us,name ='about'),
    # path('view_us/', view_us,name ='view'), 

    # path("contact_us/"),contact_us,name ='contact'),
] 
from django.urls import path
from Webapp import views
urlpatterns = [
    path('', views.webpage, name="webpage"),
    path('Aboutuspage/', views.Aboutuspage, name="Aboutuspage"),
    path('Contactuspage/', views.Contactuspage, name="Contactuspage"),
    path('Productdisplay/<itemCatg>', views.Productdisplay, name="Productdisplay"),
    path('Singleproduct/<int:dataid>', views.Singleproduct, name="Singleproduct"),
    path('Addtocart/<int:dataid>', views.Addtocart, name="Addtocart"),
    path('CheckOut/', views.CheckOut, name="CheckOut"),
    path('Checkoutsave/', views.Checkoutsave, name="Checkoutsave"),
    path('Login/', views.Login, name="Login"),
    path('Loginsave/', views.Loginsave, name="Loginsave"),
    path('Customerlogin/', views.Customerlogin, name="Customerlogin"),
    path('Customerlogout/', views.Customerlogout, name="Customerlogout"),
    path('Contactsave/', views.Contactsave, name="Contactsave")
]
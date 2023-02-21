from django.urls import path
from Demoapp import views

urlpatterns = [
    path('samplepage/', views.samplepage, name="samplepage"),
    path('Adminpage/', views.Adminpage, name="Adminpage"),
    path('Adminsave/', views.Adminsave, name="Adminsave"),
    path('Displayadmin/', views.Displayadmin, name="Displayadmin"),
    path('Editadmin/<int:dataid>/', views.Editadmin, name='Editadmin'),
    path('Updateadmin/<int:dataid>/', views.Updateadmin, name='Updateadmin'),
    path('Deleteadmin/<int:dataid>/', views.Deleteadmin, name="Deleteadmin"),
    path('Addcategory/', views.Addcategory, name="Addcategory"),
    path('Categorysave/', views.Categorysave, name="Categorysave"),
    path('DisplayCategory/', views.DisplayCategory, name="DisplayCategory"),
    path('Editcategory/<int:dataid>/', views.Editcategory, name="Editcategory"),
    path('Updatecategory/<int:dataid>/', views.Updatecategory, name="Updatecategory"),
    path('Deletecategory/<int:dataid>/', views.Deletecategory, name="Deletecategory"),
    path('Addproduct/', views.Addproduct, name="Addproduct"),
    path('Productsave/', views.Productsave, name="Productsave"),
    path('Displayproduct/', views.Displayproduct, name="Displayproduct"),
    path('Editproduct/<int:dataid>/', views.Editproduct, name="Editproduct"),
    path('Updateproduct/<int:dataid>/', views.Updateproduct, name="Updateproduct"),
    path('Deleteproduct/<int:dataid>/', views.Deleteproduct, name="Deleteproduct"),
    path('Adminloginpage/', views.Adminloginpage, name="Adminloginpage"),
    path('Adminlogin/', views.Adminlogin, name="Adminlogin"),
    path('Adminlogout/', views.Adminlogout, name='Adminlogout')
]
from django.urls import path
from WebApp import views


urlpatterns=[
    path('Home/',views.home_page,name="Home"),
    path('About/',views.about_page,name="About"),
    path('Our_Products/',views.product_page,name="Our_Products"),
    path('Services/',views.services,name="Services"),
    path('Contact/',views.contact,name="Contact"),
    path('Filtered_items/<cat_name>',views.filtered_items,name="Filtered_items"),
    path('Single_item/<int:item_id>/',views.single_item,name="Single_item"),
    path('Save_contact/',views.save_contact_details,name="save_contact_details"),
    path('',views.sign_in,name="Sign_In"),
    path('Sign_Up/',views.sign_up,name="Sign_Up"),
    path('Save_Signup/',views.save_signup,name="Save_Signup"),
    path('User_Login/',views.user_login,name="User_Login"),
    path('User_Logout/',views.user_logout,name="User_Logout"),
    path('Save_Cart/',views.save_cart,name="Save_Cart"),
    path('Cart_Page/', views.cart_page,name="Cart_Page"),
    path('Delete_Cart/<int:cart_id>/', views.delete_cart, name="Delete_Cart"),
    path('Checkout_Page/',views.checkout_page,name="Checkout_Page"),
    path('Save_Checkout/',views.save_checkout,name="Save_Checkout"),
    path('Payment_Page/',views.payment_page,name="Payment_Page"),


]
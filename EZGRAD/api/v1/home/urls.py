from django.urls import path
from api.v1.home import views

urlpatterns=[
    path('add-homedetails/',views.add_homedetails),
    path('view-homedetails/',views.view_homedetails),
    path('edit-homedetails/<int:id>',views.edit_homedetails),
    path('delete-homedetails/<int:id>',views.delete_homedetails),


    path('add-contact/',views.add_contact),
    path('view-contact/',views.view_contact),
    path('edit-contact/<int:id>',views.edit_contact),
    path('delete-contact/<int:id>',views.delete_contact),

    path('add-details/',views.add_details),
    path('view-details/',views.view_details),
    path('edit-details/<int:id>',views.edit_details),
    path('delete-details/<int:id>',views.delete_details),


    path('add-experts/',views.add_experts),
    path('view-experts/',views.view_experts),
    path('edit-experts/<int:id>',views.edit_experts),
    path('delete-experts/<int:id>',views.delete_experts),

]
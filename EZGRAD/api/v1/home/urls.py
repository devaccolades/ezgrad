from django.urls import path
from api.v1.home import views

urlpatterns=[
    path('add-homedetails/',views.add_homedetails),
    path('view-homedetails/',views.view_homedetails),
    path('edit-homedetails/<int:id>',views.edit_homedetails),
    path('delete-homedetails/<int:id>',views.delete_homedetails),
    path('hide-homedetails/<int:id>',views.hide_homedetails),
    path('list-homedetails/',views.list_homedetails),

    path('add-subbanner/',views.add_subbanner),
    path('view-subbanner/',views.view_subbanner),
    path('edit-subbanner/<int:id>',views.edit_subbanner),
    path('delete-subbanner/<int:id>',views.delete_subbanner),
    path('hide-subbanner/<int:id>',views.hide_subbanner),
    path('list-subbanner/',views.list_subbanner),


    path('add-contact/',views.add_contact),
    path('view-contact/',views.view_contact),
    path('edit-contact/<int:id>',views.edit_contact),
    path('delete-contact/<int:id>',views.delete_contact),
    path('list-contact/',views.list_contact),

    path('add-details/',views.add_details),
    path('view-details/',views.view_details),
    path('edit-details/<int:id>',views.edit_details),
    path('delete-details/<int:id>',views.delete_details),
    path('list-details/',views.list_details),


    path('add-experts/',views.add_experts),
    path('view-experts/',views.view_experts),
    path('edit-experts/<int:id>',views.edit_experts),
    path('delete-experts/<int:id>',views.delete_experts),
    path('list-experts/',views.list_experts),

]
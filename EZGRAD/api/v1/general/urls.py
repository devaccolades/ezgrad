from django.urls import path
from api.v1.general import views


urlpatterns=[
    path('add-register/',views.add_register),
    path('view-register/',views.view_register),
    path('edit-register/<pk>',views.edit_register),
    path('delete-register/<pk>',views.delete_register),
    # path('login/',views.UserLogin),
  

]
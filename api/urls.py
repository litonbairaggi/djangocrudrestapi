from django.urls import path
from api import views 

urlpatterns = [    
    path('get', views.get_admission),
    path('get/<int:pk>', views.get_admission_detail),
    path('post', views.post_admission),
    path('post/<int:pk>', views.post_admission_detail),
    path('put/<int:pk>', views.update_admission),
    path('delete/<int:pk>', views.delete_admission),
]
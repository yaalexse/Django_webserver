from django.urls import path
from . import views
from .views import new_auth
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('Codes/', views.ino.as_view(), name='Ino'),
    path('authors/',new_auth.as_view(), name='auth'),
    path('Codes/<uuid:pk>', views.code__detail.as_view() , name='code-detail'),
    path('Codes/new/', views.edit_new_code_, name = 'edit_a_new_code'),
    path('Codes/new/compil', views.compil_this_fcking_code, name = 'compil_code')
]
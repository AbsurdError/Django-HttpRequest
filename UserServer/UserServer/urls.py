from app import views
from django.urls import path, re_path

urlpatterns = [
    path('', views.index),
    path('error', views.error),
    re_path(r'^user/(?P<login>\w+)/(?P<name_folder>\w+)/(?P<number_post>\d+)', views.user),
    re_path(r'^user/(?P<login>\w+)/(?P<name_folder>\w+)', views.user),
    re_path(r'^user/(?P<login>\w+)', views.user),
    re_path(r'^user', views.user)
]
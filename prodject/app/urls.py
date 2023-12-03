from django.urls import path, re_path
from .views import index

urlpatterns = [
    path('', index),
    re_path(r'^user/(?P<name>\D+)/(?P<age>\d+)', index),
    # path('user/<str:name>/<int:age>', index, name='home'), #http://127.0.0.1:8000/app/user/Tom/age
    re_path(r'^user/(?P<name>\D+)', index),
    # path('user/<str:name>', index, name='home'),
    re_path(r'^user', index)
    # path('user', index, name='home')
]
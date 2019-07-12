from django.urls import path, re_path, include
from menu_util.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='item'),
    re_path(r'^(.*)/$', IndexView.as_view(), name='item'),
]
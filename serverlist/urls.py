from django.conf import settings
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', ServerList.as_view(), name='home'),
    path('info/<int:pk>/', ServerInfo.as_view(), name='info'),
    path('create/', CreateServer.as_view(), name='create'),
    path('create/<int:pk>', CreateServer.as_view(), name='create_child'),
    path('update/<int:pk>', UpdateServer.as_view(), name='update'),
    path('delete/<int:pk>', DeleteServer.as_view(), name='delete'),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns

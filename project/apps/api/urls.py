from django.urls import path, include

urlpatterns = [
    path('account/', include('apps.accounts.urls')),
    path('crud/', include('apps.crud.urls'))
]
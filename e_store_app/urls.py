
from django.urls import path

from e_store_app.views import index_view

urlpatterns = [
    path('', index_view, name='index')
]

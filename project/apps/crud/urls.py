from django.urls import path

from .views import *

urlpatterns = [
    path('listModels', ListModelsView.as_view()),
    path('getModel', GetModelView.as_view()),
    path('updateModel', UpdateModelView.as_view()),
    path('removeModelData', DeleteModelDataView.as_view()),
    path('addItem', AddItemView.as_view()),
]
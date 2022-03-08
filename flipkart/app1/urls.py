from django.urls import path
from .views import OrderInfo,OrderDetail


urlpatterns  =[

    path("order/", OrderDetail.as_view()),
    path("order/<int:id>/", OrderInfo.as_view())


]
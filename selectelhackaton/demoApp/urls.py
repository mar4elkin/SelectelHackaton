from django.urls                import path, include, re_path

from .views                     import *

urlpatterns = [
    path("order/<int:pk>", order_ditail, name="order_ditail")
] 

from django.urls import path
from .views import CategorViewSet , CategoryAPIView

urlpatterns = [
    
    # path('categories/', CategoryAPIView.as_view()),
    # path('categories/<slug:slug>/', CategoryAPIView.as_view()),
]
#     path('category/', CategorViewSet.as_view({'get': 'list'})),
#     path('category/<int:pk>/', CategorViewSet.as_view({'get': 'retrieve'})),
#     path('category_apiview/', CategoryAPIView.as_view()),
# ]
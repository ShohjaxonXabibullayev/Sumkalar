from django.urls import path
from .views import *

#function based view uchun

# urlpatterns = [
#     path('', List, name='List'),
#     path('detail/<int:pk>/', detail, name='detail'),
    # path('create/', create, name='create'),
#     path('update/<int:pk>/', update, name='update'),
#     path('delete/<int:pk>/', delete, name='delete')
# ]

#APIView uchun

# urlpatterns = [
#     path('', APIViewList.as_view(), name='list')
# ]

#GenericAPIView uchun

urlpatterns = [
    path('', GenericList.as_view(), name='list'),
    path('create/', Create.as_view(), name='create'),
    path('update/<int:pk>/', Update.as_view(), name='update'),
]

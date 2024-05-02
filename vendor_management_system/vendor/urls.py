# urls.py
from django.urls import path
from .views import (VendorCreateAPIView, VendorListAPIView, VendorDestroyAPIView,
                    VendorRetrieveAPIView,VendorUpdateAPIView)

urlpatterns = [
    path('api/vendor/', VendorCreateAPIView.as_view(), name='create_vendor'),
    path('api/vendors/', VendorListAPIView.as_view(), name='list_vendor'),
    path('api/vendors/<int:pk>', VendorRetrieveAPIView.as_view(), name='detail_vendor'),
    path('api/vendors/<int:pk>/delete', VendorDestroyAPIView.as_view(), name='delete_vendor'),
    path('api/vendors/<int:pk>/update', VendorUpdateAPIView.as_view(), name='update_vendor'),
]

from django.shortcuts import render
from rest_framework import generics
from vendor.serializers import VendorSerializer
from vendor.models import Vendor

class VendorCreateAPIView(generics.CreateAPIView):
    """Views for Create New Vendor"""
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class VendorListAPIView(generics.ListAPIView):
    """Views for List all Vendors"""
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class VendorRetrieveAPIView(generics.RetrieveAPIView):
    """Views for Retrieve Single Vendor"""
    serializer_class = VendorSerializer
    queryset = Vendor.objects.all()


class VendorDestroyAPIView(generics.DestroyAPIView):
    """Views for Delete Vendor"""
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class VendorUpdateAPIView(generics.UpdateAPIView):
    """Views for Update Vendor"""
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    http_method_names = ['patch', 'options']


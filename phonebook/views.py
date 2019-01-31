from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .serializers import ContactSerializer
from .models import Contact
from django_filters.rest_framework import DjangoFilterBackend
#from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import CursorPagination



class ContactsList(ListCreateAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('contact_name', 'email')

class IndividualContact(RetrieveUpdateDestroyAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer



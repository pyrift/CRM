from .serializers import ClinetsSerializer
from .models import Client
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework import generics
from django.template import loader
from django.http import HttpResponse
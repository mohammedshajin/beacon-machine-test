from django.shortcuts import render
from django.db.models import manager
from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


@api_view(['Get'])
def getRoutes(request):
    routes = [
        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'},
    ]

    return Response(routes)

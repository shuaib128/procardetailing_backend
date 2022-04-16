from django.shortcuts import render
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class Mainview(APIView):
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def post(self, request, format=None):
        return Response("serilizer.data")
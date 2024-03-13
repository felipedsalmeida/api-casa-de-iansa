from django.shortcuts import render, get_list_or_404

from rest_framework.views import APIView, Request, Response, status
from .serializers import MediumSerializer
from .models import Medium

# Create your views here.

class MediumView(APIView):
    def get(self, request: Request) -> Response:
        mediuns = Medium.objects.all()

        serializer = MediumSerializer(mediuns, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request: Request) -> Response:
        serializer = MediumSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()


        return Response(serializer.data, status=status.HTTP_201_CREATED)
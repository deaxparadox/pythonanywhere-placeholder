from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from .serializers import UserInfoModelSerializer
from ..models import UserInfo

class ListView(generics.ListAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoModelSerializer

    def get_queryset(self):
        return super().get_queryset()


@api_view(["GET"])
def get_user_info_view(request, id):
    """
    Accept only GET request
    """
    match request.method:
        case "GET": 
            query_set = None
            try:
                query_set = UserInfo.objects.get(id=id)
                # print(query_set)
            except UserInfo.DoesNotExist as e:
                return Response(status=status.HTTP_404_NOT_FOUND)
            
            
            serializer = UserInfoModelSerializer(query_set)
            # print(serializer.data)
            # json = JSONRenderer().render(serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        case _: 
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
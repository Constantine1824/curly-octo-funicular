from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from django.conf import settings
from .serializers import UserCreationSerializer
from rest_framework import status
from .signals import send_verification_email
from .utils import UrlSign
from .models import User

class CreateAccountApiView(APIView):
    def post(self, request):
        data = request.data
        serializer = UserCreationSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
class VerifyAccountApiView(APIView):
    def get(self, request, token):
        try:
            username = UrlSign().url_decode(token)
            user_obj = User.objects.get(username = username)
            user_obj.is_active = True
            user_obj.save()
            if settings.ACTIVATION_REDIRECT_URL is not None:
                return HttpResponseRedirect(settings.ACTIVATION_REDIRECT_URL)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            print(e)
            return Response(
                {
                    'status' : 'Error',
                    'detail' : 'Invalid Token'
                }
            )

        

# Create your views here.

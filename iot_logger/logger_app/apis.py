from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from  drf_yasg import openapi
from  rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination

from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import  method_decorator

from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from .serializers import LogSerializer,SendEmailSerializer
from .models import Log

class LogViewSet(ModelViewSet):
    serializer_class = LogSerializer
    queryset = Log.objects.all()
    permission_classes= (AllowAny,) #For now, it is open
    # permission_classes = (permissions.IsAuthenticated,IsOwner)



class SendEmailView(APIView):
    serializer_class = SendEmailSerializer
    permission_classes= (AllowAny,) #For now, it is open
    # parser_classes = (FormParser, MultiPartParser)
    
    
    @swagger_auto_schema(request_body=SendEmailSerializer)    
    def post (self,request):
  
        serializer = SendEmailSerializer(data=request.data)
        
        if  serializer.is_valid():
            senders = serializer.validated_data['senders']
            subject =  serializer.validated_data['subject']
            message = serializer.validated_data['message']
            from_email =settings.EMAIL_HOST_USER
            to_list = senders #[sender]
            print(message)
            # try:
            send_mail(subject, message, from_email, to_list, fail_silently=False)
            print("Kindly check your mail for the alert")  
        
            return Response({
                'code':200,
                'status':'success',
                'message':'Email Sent',
                },status=status.HTTP_200_OK)
            # except :
            #     return Response({'code':400,
            #         'status':'error',
            #         'message':'Error occurred when sending mail. Kindly contact your admin'},status=status.HTTP_400_BAD_REQUEST)
                        
        else:
            return Response({'code':400,
                    'status':'error',
                    'message':'Check the input data. Kindly contact your admin'},status=status.HTTP_400_BAD_REQUEST)
                        
        
              
@method_decorator(
    name='get', decorator=swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'limit', openapi.IN_QUERY, description="Number of results to return per page.", type=openapi.TYPE_INTEGER
            ),
            openapi.Parameter(
                'offset', openapi.IN_QUERY, description="The initial index from which to return the results.", type=openapi.TYPE_INTEGER
            ),
            
            openapi.Parameter(
                'date_start', openapi.IN_QUERY, description=" date to start filtering", type=openapi.FORMAT_DATE
                ),
            openapi.Parameter(
                'date_end', openapi.IN_QUERY, description=" date to end filtering", type=openapi.FORMAT_DATE
                ),
            openapi.Parameter(
                'device_id', openapi.IN_QUERY , description="device_id to filter", type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                'location_id', openapi.IN_QUERY , description="location_id to filter", type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                'level', openapi.IN_QUERY , description="level to filter such as : warning,error,debug,critical,etc", type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                'topic', openapi.IN_QUERY , description="mqtt broker topic", type=openapi.TYPE_STRING
            ),
            ],
        )
    )
class GetLogDataView(APIView):
    permission_classes= (AllowAny,) #For now, it is open

    # permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        
        date_start = self.request.query_params.get('date_start')
        date_end = self.request.query_params.get('date_end')
        device_id = self.request.query_params.get('device_id')
        location_id = self.request.query_params.get('location_id')
        level = self.request.query_params.get('level')
        topic = self.request.query_params.get('topic')
        
        queryset = Log.objects.all().order_by('-id')
        
        if date_end  and date_start :
            queryset = queryset.objects.filter( created_date__gte=date_start,created_date__lte=date_end).order_by('-id')
            
        elif device_id:
            queryset =queryset.objects.filter(device_id=device_id)
        
        elif location_id:
            queryset =queryset.filter(location_id=location_id)
        
        elif level:
            queryset=queryset.filter(level=level)
        
        elif topic:
            queryset=queryset.filter(mqtt_topic=topic)
        else:
            queryset = queryset
            
        if not queryset:
            
            return Response(
                {'code': 200,
                    'status':'success',
                    'message': 'No data',
                    'data':{'results':[]}
                }, status=status.HTTP_200_OK)
                
        else:
            serializer = LogSerializer
            paginator = LimitOffsetPagination()   
            result_page = paginator.paginate_queryset(queryset.order_by('-id'), request) 
            serializer = serializer(result_page, many=True)
            result=paginator.get_paginated_response(serializer.data)
            output = result.data
            return Response(
                {
                    'code': 200,
                    'status':'success',
                    'message': 'Data pulled successfully',
                    'data':output
                }, status=status.HTTP_200_OK)  

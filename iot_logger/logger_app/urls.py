from django.urls import path
from .apis import  LogViewSet,SendEmailView,GetLogDataView
from rest_framework.routers import DefaultRouter
 
router = DefaultRouter()


router.register('logs',LogViewSet, 'logs')

urlpatterns = router.urls

urlpatterns += [
    path('send-email/',SendEmailView.as_view(), name="send_email"),
    path('get/logs/',GetLogDataView.as_view(), name='get_log_data'),
]
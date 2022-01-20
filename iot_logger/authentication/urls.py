from django.urls import path
from .apis import  *
from rest_framework.routers import DefaultRouter
 
router = DefaultRouter()


# router.register('business',BusinessViewSet, 'business')
# router.register('users',UserViewSet, 'users')
# router.register('invite-members',InviteMemberViewSet,'invite-members')

urlpatterns = router.urls

urlpatterns += [

    # path('login/',LoginView.as_view(), name='login'),
    # path('change/password/',UpdatePasswordView.as_view(), name='change-password'),
    # path('confirm/otp/',OTPVerificationView.as_view(), name='confirm-otp'),
    # path('reset-password/code/',ResetPasswordEmailView.as_view(), name='reset-password-link'),
    # path('reset-password/verify-code/',ConfirmResetTokenView.as_view(), name='reset-password-verify-code'),
    # path('reset-password/',ResetPasswordView.as_view(), name='reset-password'),

    
    
    
    
]
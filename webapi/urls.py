from django.conf.urls import url
from .viewUser import UserCreateAPIView,UserLoginAPTView ,UserAPIViewList,UserRudView
from .viewSalle import SalleAPIViewList ,SalleAPIView ,SalleRudView
from .viewReservation import ReservationAPIViewList ,ReservationAPIView ,ReservationRudView
from django.conf.urls import include
from rest_framework_jwt.views import refresh_jwt_token

urlpatterns = [

    url(r'^(?P<matricule>\d+)/$',UserRudView.as_view(), name='post-rud'),
    url(r'^$',UserCreateAPIView.as_view(), name='post-create'),
    url(r'^login$', UserLoginAPTView.as_view(), name='login'),
    url(r'^list/$',UserAPIViewList.as_view(), name='post-list'),
    url(r'^lists/$',SalleAPIViewList.as_view(), name='post-list'),
    url(r'posts/$',SalleAPIView.as_view(), name='post-create'),
    url(r'^salle/(?P<salle_id>\d+)/$',SalleRudView.as_view(), name='post-rud'),
    url(r'^listr/$',ReservationAPIViewList.as_view(), name='post-list'),
    url(r'postr/$',ReservationAPIView.as_view(), name='post-create'),
    url(r'^reservation/(?P<reservation_id>\d+)/$',ReservationRudView.as_view(), name='post-rud'),
    url(r'^', include('rest_auth.urls')),
    url(r'^registration/', include('rest_auth.registration.urls')),
    url(r'^refresh-token/', refresh_jwt_token),


    
]
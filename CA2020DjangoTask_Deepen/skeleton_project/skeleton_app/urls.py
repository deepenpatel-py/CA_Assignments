from django.urls import path, include
from rest_framework import routers
from . import views

router=routers.DefaultRouter()
router.register(r'blogapi',views.BlogViewSet)

urlpatterns=[
    path('',views.HomePageView.as_view(),name='home'),
    path('blog',views.BlogPageView.as_view(),name='blog'),
    path('',include(router.urls)),
]
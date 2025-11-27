from django.urls import include, path
from rest_framework import routers
from quickstart import  views

router = routers.DefaultRouter()
router.register(r"users", views.UserViewset)
router.register(r"groups", views.GroupViewset)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framwork"))
]
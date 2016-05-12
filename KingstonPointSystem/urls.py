from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from points.views import PointViewSet

router = DefaultRouter()
router.register(r'points', PointViewSet)

urlpatterns = [
    # url(r'^$', 'points.views.detail', name='home'),
    url(r'^', include(router.urls)),

    url(r'^admin/', include(admin.site.urls)),
]

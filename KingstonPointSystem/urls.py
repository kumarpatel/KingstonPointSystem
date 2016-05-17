from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from points.views import PointViewSet, DashboardViewSet, AliasViewSet, MockService

router = DefaultRouter()
router.register(r'points', PointViewSet)
router.register(r'alias', AliasViewSet)
router.register(r'dashboards', DashboardViewSet, base_name="dashboard-list")
router.register(r'mock', MockService, base_name="mock-list")

urlpatterns = [
    # url(r'^$', 'points.views.detail', name='home'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
]


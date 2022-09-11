from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.contrib import admin
from addresses import views
# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('addresses/',views.address_list),
    path('addresses/<int:pk>/', views.address),
    path('login/', views.login),
    path('pages/login', views.login_page),
    path('app_login/', views.app_login),
    path('login/', include('login.urls')),
    path('todo/',include('todo.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

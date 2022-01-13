{%- if cookiecutter.use_users_example == 'y' %}
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('users', views.UserViewSet, basename='users')

urlpatterns = router.urls
{%- endif %}

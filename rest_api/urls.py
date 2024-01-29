from rest_framework.routers import SimpleRouter
from rest_api.views import RegisterModelViewSet

app_name = 'rest_api'
router = SimpleRouter(trailing_slash=False)
router.register('register', RegisterModelViewSet, basename='register')

urlpatterns = [

]
urlpatterns += router.urls

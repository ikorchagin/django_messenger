from django.urls import path
from rest_framework.routers import SimpleRouter

from chats.views import ChatsViewSet

router = SimpleRouter()
router.register('', ChatsViewSet, basename='chats')

urlpatterns = router.urls

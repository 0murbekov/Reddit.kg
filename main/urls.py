from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from posts.views import *


router = DefaultRouter()
router.register('posts', PostsViewSet)
router.register('comment', CommentViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('v1/api/categories/', CategoryListView.as_view()),
    path('v1/api/add-image/', PostImageView.as_view()),
    path('v1/api/account/', include('user.urls')),
    path('v1/api/', include(router.urls)),
    path('v1/api/posts/<int:pk>/like/', LikeView.as_view()),
    path('v1/api/posts/<int:pk>/favorite/', FavoriteView.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

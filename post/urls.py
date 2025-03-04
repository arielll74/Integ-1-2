from django.urls import path
from .views import PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('v1/api/post/', PostListCreateAPIView.as_view(), name='list-create-post'),
    path('v1/api/post/<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view(), name='retrieve-update-delete-post')
]
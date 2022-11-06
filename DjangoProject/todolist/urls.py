from django.urls import path
from . import views
from . views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='todolist-home'),
    path('task/<int:pk>/', PostDetailView.as_view(), name='task-detail'),
    path('task/new/', PostCreateView.as_view(), name='task-create'),
    path('task/<int:pk>/update/', PostUpdateView.as_view(), name='task-update'),
    path('task/<int:pk>/delete/', PostDeleteView.as_view(), name='task-delete'),
    path('about/', views.about, name='todolist-about'),
]


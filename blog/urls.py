from django.urls import path
from .views import (
    MapView, PostDetail, PostList, PostLike, SignUpView, LoginView, LogoutView,
    ProfileView, EditProfileView, DeleteAccountView, PostCreateView, PostListView,
    CommentUpdateView, CommentDeleteView, PostUpdateView, PostDeleteView
)
from django.contrib import admin
from django.urls import include

urlpatterns = [
    # Home and overview pages
    path('', PostList.as_view(), name='home'),
    path('blog-overview/', PostListView.as_view(), name='blog_overview'),
    
    # Post management
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('post/<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('post/<slug:slug>/update/', PostUpdateView.as_view(), name='update_post'),
    path('post/<slug:slug>/delete/', PostDeleteView.as_view(), name='delete_post'),
    path('like/<slug:slug>/', PostLike.as_view(), name='post_like'),
    
    # User management
    path('signup/', SignUpView.as_view(), name='account_signup'),
    path('login/', LoginView.as_view(), name='account_login'),
    path('logout/', LogoutView.as_view(), name='account_logout'),
    path('profile/', ProfileView.as_view(), name='account_profile'),
    path('profile/edit/', EditProfileView.as_view(), name='account_edit_profile'),
    path('profile/delete/', DeleteAccountView.as_view(), name='account_delete'),

    # Comment management
    path('comment/<int:pk>/edit/', CommentUpdateView.as_view(), name='edit_comment'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete_comment'),

    # Additional features
    path('map/', MapView.as_view(), name='map'),
]
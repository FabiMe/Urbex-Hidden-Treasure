from django.urls import path
from .views import (MapView, PostDetail, PostList, PostLike, SignUpView, LoginView, LogoutView,
                    ProfileView, EditProfileView, DeleteAccountView, PostCreateView, PostListView)
from django.contrib import admin
from django.urls import include

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('map/', MapView.as_view(), name='map'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('blog-overview/', PostListView.as_view(), name='blog_overview'),  
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>/', PostLike.as_view(), name='post_like'),
    path('signup/', SignUpView.as_view(), name='account_signup'),
    path('login/', LoginView.as_view(), name='account_login'),
    path('logout/', LogoutView.as_view(), name='account_logout'),
    path('profile/', ProfileView.as_view(), name='account_profile'),
    path('profile/edit/', EditProfileView.as_view(), name='account_edit_profile'),
    path('profile/delete/', DeleteAccountView.as_view(), name='account_delete'),
    path('login/', LoginView.as_view(), name='account_login'),  
]
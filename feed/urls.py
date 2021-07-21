from django.urls import path
from . import views


app_name = 'feed'

urlpatterns = [
    path("", views.HomePage.as_view(), name="index"),
    path("detail/<int:pk>/", views.PostDetailView.as_view(), name="detail"),
    path("new/", views.CreateNewPost.as_view(), name="new_post"),
]

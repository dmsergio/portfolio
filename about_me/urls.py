from django.urls import path
from . import views

urlpatterns = [
    path("", views.about_me_index, name="about_me_index"),
    # path("<int:pk>/", views.blog_detail, name="blog_detail"),
    # path("<category>/", views.blog_category, name="blog_category"),
]

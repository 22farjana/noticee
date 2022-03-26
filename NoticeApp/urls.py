from django.urls import path

from .views import HomeView
from . import views
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path("<int:postid>/", views.comment, name='idshow'),
    path('json',views.json),
    path('blog',views.blog)

]

from django.urls import path

from .views import (
    IndexView,
    NewsPaperDetail,
    NewsPaperUpdate,
    UserNewsList,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("newspaper/<int:pk>/", NewsPaperDetail.as_view(), name="newspaper"),
    path("newspaper/<int:pk>/edit/", NewsPaperUpdate.as_view(), name="edit"),
    path("my-news/", UserNewsList.as_view(), name="my_news"),
]

app_name = "news"
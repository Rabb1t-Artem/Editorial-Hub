from django.urls import path

from .views import (
    IndexView,
    NewsPaperCreate,
    NewsPaperDetail,
    NewsPaperUpdate,
    UserNewsList,
    TopicList,
    TopicDetail,
    TopicCreate,
    TopicUpdate,
    NewsPaperDelete,
    TopicDelete,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("my-news/", UserNewsList.as_view(), name="my_news"),
    path("newspaper/<int:pk>/", NewsPaperDetail.as_view(), name="newspaper"),
    path("newspaper/<int:pk>/edit/", NewsPaperUpdate.as_view(), name="edit"),
    path("newspaper/create/", NewsPaperCreate.as_view(), name="create"),
    path(
        "newspaper/update/<int:pk>/", NewsPaperUpdate.as_view(), name="update"
    ),
    path(
        "newspaper/delete/<int:pk>/", NewsPaperDelete.as_view(), name="delete"
    ),
    path("topics/", TopicList.as_view(), name="topic-list"),
    path("topic/<int:pk>/", TopicDetail.as_view(), name="topic-detail"),
    path("topic/create/", TopicCreate.as_view(), name="topic-create"),
    path("topic/update/<int:pk>/", TopicUpdate.as_view(), name="topic-update"),
    path("topic/delete/<int:pk>/", TopicDelete.as_view(), name="topic-delete"),
]

app_name = "news"

from django.urls import path

from .views import (
    IndexView,
    NewsPaperDetail
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("newspaper/<int:pk>/", NewsPaperDetail.as_view(), name="newspaper"),
    # path("newspaper/<int:pk>/detail/", NewsPaperDetail.as_view(), name="newspaper_detail"),
]

app_name = "news"
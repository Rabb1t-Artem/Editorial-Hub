from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from news.models import Newspaper


class IndexView(generic.ListView):
    model = Newspaper
    template_name = "news/index.html"
    context_object_name = "news"


class NewsPaperDetail(generic.DetailView):
    model = Newspaper
    template_name = "news/newspaper_detail.html"


class UserNewsList(LoginRequiredMixin, generic.ListView):
    model = Newspaper
    template_name = "news/user_news_list.html"
    context_object_name = "news_list"

    def get_queryset(self):
        return Newspaper.objects.filter(redactor=self.request.user)


class NewsPaperUpdate(LoginRequiredMixin, generic.UpdateView):
    pass

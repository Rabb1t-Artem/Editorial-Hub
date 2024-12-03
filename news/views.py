from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from news.models import Newspaper


class IndexView(generic.TemplateView):
    template_name = "news/index.html"


class NewsPaperDetail(generic.DetailView):
    model = Newspaper


class NewsPaperUpdate(LoginRequiredMixin, generic.UpdateView):
    pass

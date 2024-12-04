from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q

from news.models import Newspaper, Topic
from news.forms import NewspaperForm, NewsSearchForm


class IndexView(generic.ListView):
    model = Newspaper
    template_name = "news/index.html"
    context_object_name = "news"

    def get_queryset(self):
        queryset = Newspaper.objects.all()
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(
                Q(title__icontains=q) |
                Q(description__icontains=q)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = NewsSearchForm(self.request.GET)
        return context



#--------------------NewsPaper------------------------------------------------

class NewsPaperDetail(generic.DetailView):
    model = Newspaper
    template_name = "news/newspaper_detail.html"


class UserNewsList(LoginRequiredMixin, generic.ListView):
    model = Newspaper
    template_name = "news/user_news_list.html"
    context_object_name = "news_list"

    def get_queryset(self):
        queryset = Newspaper.objects.filter(redactor=self.request.user)
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(
                Q(title__icontains=q) |
                Q(description__icontains=q)
            )
        return queryset


class NewsPaperCreate(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    form_class = NewspaperForm
    template_name = "news/newspaper_form.html"
    success_url = reverse_lazy("news:my_news")

    def form_valid(self, form):
        form.instance.redactor = self.request.user
        return super().form_valid(form)


class NewsPaperUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    form_class = NewspaperForm
    template_name = "news/newspaper_form.html"
    success_url = reverse_lazy("news:my_news")


#--------------------Topics---------------------------------------------------


class TopicList(generic.ListView):
    model = Topic
    template_name = "news/topic_list.html"
    context_object_name = "topics"


class TopicDetail(generic.DetailView):
    model = Topic
    template_name = "news/topic_detail.html"
    context_object_name = "topic"
    queryset = Topic.objects.all().prefetch_related('newspapers')


class TopicCreate(LoginRequiredMixin, generic.CreateView):
    model = Topic
    fields = ['name']
    template_name = "news/topic_form.html"
    success_url = reverse_lazy("news:topic-list")


class TopicUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    fields = ['name']
    template_name = "news/topic_form.html"
    success_url = reverse_lazy("news:topic-list")

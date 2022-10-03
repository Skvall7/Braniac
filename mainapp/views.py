import json
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from mainapp.apps import MainappConfig


app_name = MainappConfig.name


class MainPageView(TemplateView):
    template_name = 'mainapp/index.html'


class NewsPageView(TemplateView):
    template_name = 'mainapp/news.html'
    with open('news.json', encoding='utf-8') as f:
        news_json = json.load(f)['news']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['range'] = range(1, 6)
        context['News'] = self.news_json      # datetime.now()

        return context


class NewsWithPaginatorView(NewsPageView):

    def get_context_data(self, page,  **kwargs):
        context = super().get_context_data(page=page, **kwargs)
        context['page_num'] = page
        return context


class CoursesPageView(TemplateView):
    template_name = 'mainapp/courses_list.html'


class ContactsPageView(TemplateView):
    template_name = 'mainapp/contacts.html'


class DocSitePageView(TemplateView):
    template_name = 'mainapp/doc_site.html'


class LoginPageView(TemplateView):
    template_name = 'mainapp/login.html'


def check_kwargs(request, **kwargs):
    return HttpResponse(f'kwargs:<br>{kwargs}')

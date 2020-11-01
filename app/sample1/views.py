from django.shortcuts import render

from django.views.generic.base import TemplateView
from sample1.models import Article

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['latest_articles'] = Article.objects.all()[:5]
        return context

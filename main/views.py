from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from django.urls import reverse

from django.urls import reverse


class HomeView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        search_name = request.GET.get('search_name')
        search_surname = request.GET.get('search_surname')

        if search_name or search_surname:
            url = reverse('jobs:find-employee') + f'?search_name={search_name}&search_surname={search_surname}'
            return redirect(url)
        return super().get(request, *args, **kwargs)


class ContactView(TemplateView):
    template_name = 'contact.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class BlogView(TemplateView):
    template_name = 'blog.html'


class BlogDetailsView(TemplateView):
    template_name = 'blog-details.html'

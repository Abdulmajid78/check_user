from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
import telegram
import telegram.error
from django.conf import settings
from django.views.generic.edit import FormMixin

from jobs.models import EmployeeModel
from .forms import ContactForm
from django.urls import reverse, reverse_lazy

from django.utils.translation import gettext_lazy as _


class HomeView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        search_name = request.GET.get('search_name')
        search_surname = request.GET.get('search_surname')

        if search_name or search_surname:
            url = reverse('jobs:find-employee') + f'?search_name={search_name}&search_surname={search_surname}'
            return redirect(url)

        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data()
        data['employees'] = EmployeeModel.objects.order_by('?')[:9]
        return data


class ContactCreateView(View, FormMixin):
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = reverse_lazy('main:contacts')

    async def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            if len(phone_number) == 11:
                return render(request, "main/contact.html", _({'error': 'Failed to send message'}))
            else:
                pass

            bot = telegram.Bot(token=settings.TELEGRAM_BOT_TOKEN)
            chat_id = settings.TELEGRAM_CHAT_ID
            message = (f"Новое сообщение от: \n name: {name}\n email: {email} \n Телефон номер: ({phone_number})"
                       f"\n subject: ({subject}) \n Сообщение: {message}")

            try:
                await bot.send_message(chat_id=chat_id, text=message)
            except telegram.error.TelegramError:
                return render(request, "main/contact.html", _({'error': 'Failed to send message'}))

            return super().form_valid(form)

        return render(request, "main/contact.html", {'form': form})

    async def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return render(request, self.template_name, {'form': form})


class ContactView(TemplateView):
    template_name = 'main/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_form'] = ContactForm()
        return context


class AboutView(TemplateView):
    template_name = 'main/about.html'


class BlogView(TemplateView):
    template_name = 'blog.html'


class BlogDetailsView(TemplateView):
    template_name = 'blog-details.html'

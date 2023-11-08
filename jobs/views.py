from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView, ListView, CreateView, DetailView
from users.models import CompanyUser
from .models import EmployeeModel, Comment, CompanyModel
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import EmployeeModelForm, CommentForm


@login_required
def add_employee(request):
    if request.method == "POST":
        form = EmployeeModelForm(request.POST)
        if form.is_valid():
            employee = form.save()  # Save the instance
            return redirect('main:home')
    else:
        form = EmployeeModelForm()
    return render(request, 'jobs/post-employee.html', {'form': form})


class FindEmployeeView(ListView):
    template_name = 'jobs/find-employee.html'
    paginate_by = 14

    def get_queryset(self):
        qs = EmployeeModel.objects.filter(is_active=True)

        search_name = self.request.GET.get('search_name')
        if search_name:
            qs = qs.filter(Q(first_name__icontains=search_name) | Q(last_name__icontains=search_name))

        search_surname = self.request.GET.get('search_surname')
        if search_surname:
            qs = qs.filter(Q(first_name__icontains=search_surname) | Q(last_name__icontains=search_surname))

        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data()
        data['employees'] = EmployeeModel.objects.all()
        return data


class EmployeeDetailView(DetailView):
    model = EmployeeModel
    template_name = 'jobs/employee-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(employee=self.object)
        context['form'] = CommentForm()
        return context


@method_decorator(login_required, name='dispatch')
class CommentCreateView(LoginRequiredMixin, CreateView):
    form_class = CommentForm
    template_name = 'jobs/comment.html'

    def form_valid(self, form):
        employee = get_object_or_404(EmployeeModel, pk=self.kwargs.get('pk'))
        form.instance.employee = employee

        if isinstance(self.request.user, CompanyUser):
            form.instance.user = self.request.user
        else:
            return HttpResponseForbidden("You don't have permission to add comments.")

        form.instance.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('jobs:employee-detail', kwargs={'pk': self.kwargs.get('pk')})


class CompanyListView(ListView):
    model = CompanyModel
    template_name = 'jobs/companies-list.html'
    paginate_by = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data()
        data['companies'] = CompanyModel.objects.all()
        return data


class CompanyDetailView(DetailView):
    model = EmployeeModel
    template_name = 'jobs/company-details.html'


class ResumeView(TemplateView):
    template_name = 'resume.html'


class JobDetailView(TemplateView):
    template_name = 'jobs/company-details.html'


class CandidatesView(TemplateView):
    template_name = 'candidate.html'


class PostJobView(TemplateView):
    template_name = 'post-job.html'




# @require_POST
# def employee_comment(request, employee_id):
#     employee = get_object_or_404(EmployeeModel, id=employee_id, status=EmployeeModel)
#     comment = None
#     # Комментарий был отправлен
#     form = CommentForm(data=request.POST)
#     if form.is_valid():
#         # Создать объект класса Comment, не сохраняя его в базе данных
#         comment = form.save(commit=False)
#         # Назначить пост комментарию
#         comment.post = employee
#         # Сохранить комментарий в базе данных
#         comment.save()
#     return render(request, 'jobs/comment.html',
#                   {'employee': employee,
#                    'form': form,
#                    'comment': comment})



# class AddReview(View):
#     def post(self, request, pk):
#         form = CommentForm(request.POST)
#         employee = EmployeeModel.objects.get(id=pk)
#         post = EmployeeModel.objects.get(pk=self.kwargs['pk'])
#         user = self.request.user
#
#         if form.is_valid():
#             company_name = self.request.user.username
#             position = form.cleaned_data['position']
#             employ_from = form.cleaned_data['employ_from']
#             employ_to = form.cleaned_data['employ_to']
#             content = form.cleaned_data['content']
#
#             form = Comment.objects.create(
#                 user=company_name,
#                 position=position,
#                 employ_from=employ_from,
#                 employ_to=employ_to,
#                 content=content,
#                 post=post
#             )
#
#             form = form.save(commit=False)
#             form.employee = employee
#             form.save()
#
#         return redirect(employee.get_absolute_url())


# @method_decorator(login_required, name='dispatch')
# class EmployeeDetailsView(DetailView):
#     model = EmployeeModel
#     template_name = 'employee-details.html'
#     context_object_name = 'employee'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['comments'] = Comment.objects.filter(post=self.object)
#         context['form'] = CommentForm()
#         print(context)  # Добавьте эту строку для отладки
#         return context
#
#
# class CommentCreateView(FormView):
#     form_class = CommentForm
#     template_name = 'employee-details.html'
#
#     def form_valid(self, form):
#         employee = get_object_or_404(EmployeeModel, pk=self.kwargs['pk'])
#         user = self.request.user
#         if not user.is_individual and isinstance(user, CompanyUser):
#             company_name = user.company_name
#             position = form.cleaned_data['position']
#             employ_from = form.cleaned_data['employ_from']
#             employ_to = form.cleaned_data['employ_to']
#             content = form.cleaned_data['content']
#
#             comment = Comment.objects.create(
#                 user=user,
#                 position=position,
#                 employ_from=employ_from,
#                 employ_to=employ_to,
#                 content=content,
#                 post=employee
#             )
#             print('commeeeeent', comment)
#
#         return redirect('jobs:employee-detail', pk=employee.pk)

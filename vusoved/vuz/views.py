from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView

from .models import University, Feedback, User
from .forms import NameForm, FeedbackForm
from django.views import View
from django.views.generic.base import TemplateView



class IndexView(ListView):
    model = University
    template_name = "vuz/index.html"
    context_object_name = 'universities'


# def university(request, slug_university):
#     unvst = get_object_or_404(University, slug=slug_university)
#     feedbacks = unvst.feedbacks.all()
#
#     test_user = User.objects.get(name='Кристина')
#
#     if request.method == "POST":
#         form = FeedbackForm(request.POST)
#         print(request)
#         if form.is_valid():
#             print(form.cleaned_data)
#             new_feedback = form.save(commit=False)
#             new_feedback.university = unvst
#             new_feedback.user = test_user
#             new_feedback.save()
#             print(f'{request.POST=}')
#         else:
#             print('form is not valid')
#
#     form = FeedbackForm()
#
#     context = {
#         'university': unvst,
#         'feedbacks': feedbacks,
#         'form': form,
#         'slug_university': slug_university
#     }
#     return render(request, "vuz/university.html", context=context)


class UniversityView(DetailView):
    model = University
    template_name = "vuz/university.html"
    context_object_name = 'university'
    slug_url_kwarg = 'slug_university'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        feedbacks = Feedback.objects.filter(university_id=context['university'].id)
        context['form'] = FeedbackForm()
        context['feedbacks'] = feedbacks
        return context

    # def post(self, request, slug_university):
    #     # потом поменять
    #     test_user = User.objects.get(name='Кристина')
    #
    #     university = University.objects.get(slug=slug_university)
    #     all_rates = [fb.rate for fb in university.feedbacks.all()]
    #
    #     form = FeedbackForm(request.POST)
    #     if form.is_valid():
    #         new_feedback = form.save(commit=False)
    #         new_feedback.university = university
    #         new_feedback.user = test_user
    #         new_feedback.save()
    #
    #         university.rating = (sum(all_rates) + new_feedback.rate) / (len(all_rates) + 1)
    #         university.save()
    #     else:
    #         print('form is not valid')
    #     return redirect(university.get_absolute_url())


class AboutView(TemplateView):
    template_name = "vuz/about.html"
    extra_context = {
        'contact_email': 'kirdanchik@yandex.ru',
    }


class FeedbackView(LoginRequiredMixin, FormView):
    template_name = "vuz/feedback.html"
    form_class = FeedbackForm

    def get_success_url(self):
        return reverse_lazy('university', kwargs={'slug_university': self.kwargs.get('slug_university', None)})

    def form_valid(self, form):
        test_user = User.objects.get(name='Кристина')

        university = University.objects.get(slug=self.kwargs['slug_university'])
        all_rates = [fb.rate for fb in university.feedbacks.all()]

        new_feedback = form.save(commit=False)
        new_feedback.university = university
        new_feedback.user = test_user
        new_feedback.save()

        university.rating = (sum(all_rates) + new_feedback.rate) / (len(all_rates) + 1)
        university.save()

        return super().form_valid(form)

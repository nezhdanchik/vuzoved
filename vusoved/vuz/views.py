from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import University, Feedback, User
from .forms import NameForm, FeedbackForm


def index(request):
    universities = University.objects.all()
    return render(request, "vuz/index.html", context={'universities': universities})


def university(request, slug_university):

    unvst = get_object_or_404(University, slug=slug_university)
    feedbacks = unvst.feedbacks.all()

    test_user = User.objects.get(name='Кристина')

    if request.method == "POST":
        form = FeedbackForm(request.POST)
        print(request)
        if form.is_valid():
            print(form.cleaned_data)
            new_feedback = form.save(commit=False)
            new_feedback.university = unvst
            new_feedback.user = test_user
            new_feedback.save()
            print(f'{request.POST=}')
        else:
            print('form is not valid')

    form = FeedbackForm()


    context = {
        'university': unvst,
        'feedbacks': feedbacks,
        'form': form,
        'slug_university': slug_university
    }
    return render(request, "vuz/university.html", context=context)


def about(request):
    context = {
        'contact_email': 'kirdanchik@yandex.ru',
    }
    return render(request, "vuz/about.html", context=context)


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        print('1232oe')
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print('data from form', form.cleaned_data)
        else:
            print('form is not valid', form.cleaned_data)
    else:
        form = NameForm()

    return render(request, "vuz/name.html", {"form": form})

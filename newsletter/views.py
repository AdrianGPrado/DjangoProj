from django.shortcuts import render

from .forms import ContactForm, SingUpForm

# Create your views here.
def home(request):
    # title = 'Welcome'
    # if request.user.is_authenticated():
    title = 'Welcome ' + str(request.user)

    print(request)
    form = SingUpForm(request.POST or None)

    context = {
        'title': title,
        'form': form,
    }

    if form.is_valid():
        instance.save()
        # instance = form.save(commit=False)
        # print(instance)
        # print(instance.timestamp)
        context['title'] = 'Thank you'

    if request.method == 'POST':
        print(request.POST)

    # add a form
    return render(request, 'home.html', context)


def contact(request):
    title = 'Contact Me'
    form = ContactForm(request.POST or None)
    title_align_center = True

    if form.is_valid():
        email = form.cleaned_data.get('email')
        full_name = form.cleaned_data.get('full_name')
        message = form.cleaned_data.get('message')
        print(form.cleaned_data)

    context = {
        'form': form,
        'title': title,
        'title_align_center': title_align_center,
    }
    return render(request, "forms.html", context)

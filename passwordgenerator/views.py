from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from passwordgenerator.forms import PasswordForm
from passwordgenerator.password import PasswordGenerator

passwordgenerator = PasswordGenerator()


def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PasswordForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            length = form.cleaned_data['length']
            special_chars = form.cleaned_data['special_chars']
            result = passwordgenerator.generate(length, special_chars)
            return render(request, 'generator.html',
                          {'form': form, "result": result, "history": passwordgenerator.get_history_limited(5)})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PasswordForm()

    return render(request, 'generator.html', {'form': form})

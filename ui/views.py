from django.shortcuts import render, redirect

from students.Passwortgenerator import PasswortGenerator
from students.Tippgeschwindigkeit import Tippgeschwindigkeit
from students.notenrechner import Notenrechner
from students.username import UsernameGenerator
from students.zufallswuerfel import Zufallswuerfel
from .forms import NoteCalculator, DiceForm, TippingForm, PasswordGeneratorForm

calc = Notenrechner(100)
zuefallswuerfel = Zufallswuerfel(6)
tipping = Tippgeschwindigkeit()


def note_calculator(request):
    global calc
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NoteCalculator(request.POST)
        # check whether it's valid:
        if form.is_valid():
            reached_points = form.cleaned_data['reached_points']
            max_points = form.cleaned_data['max_points']
            if max_points != calc.max_points:
                calc = Notenrechner(max_points)

            return render(request, 'grade.html',
                          {'form': form, 'result': calc.calculate(reached_points), 'max': calc.best(),
                           'min': calc.worst(),
                           'avg': calc.average(), 'history': calc.history()})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NoteCalculator()

    return render(request, 'grade.html', {'form': form})


def note_calculator_reset(request):
    if request.method == 'POST':
        global calc
        calc = Notenrechner(100)
        return redirect('/ui/grade/')
    else:
        return redirect('/ui/grade/')


def username(request):
    return render(request, "username.html", {"username": UsernameGenerator().generate()})


def dice(request):
    global zuefallswuerfel
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DiceForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            max_number = form.cleaned_data['max_number']
            if max_number != zuefallswuerfel.maxseiten:
                zuefallswuerfel = Zufallswuerfel(max_number)

            return render(request, 'dice.html',
                          {'form': form, 'result': zuefallswuerfel.throw(),
                           'history': zuefallswuerfel.get_last_throws()})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DiceForm()

    return render(request, "dice.html",
                  {"result": zuefallswuerfel.throw(), 'history': zuefallswuerfel.get_last_throws(),
                   "form": form})


def tipping_pace_start(request):
    global tipping

    if tipping.start():
        form = TippingForm()
        return render(request, "tipping.html", {"result": None, "form": form})
    else:
        tipping = Tippgeschwindigkeit()
        return redirect('/ui/tipping/')


def tipping_pace_end(request):
    global tipping
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TippingForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            text = form.cleaned_data['input']
            if tipping.finish(text):
                result = tipping.number_of_words_per_minute()
                tipping = Tippgeschwindigkeit()
                return render(request, 'tipping.html',
                              {'form': form, 'result': result})
            else:
                tipping = Tippgeschwindigkeit()
                return redirect('/ui/tipping/')
    else:
        tipping = Tippgeschwindigkeit()
        return redirect('/ui/tipping/')


def password(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PasswordGeneratorForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            length = form.cleaned_data['length']
            special_chars = form.cleaned_data['special_chars']
            result = PasswortGenerator()
            return render(request, "password.html",
                          {"result": "".join(result.generieren(length, special_chars)), "form": form})
    else:
        form = PasswordGeneratorForm()
        result = PasswortGenerator()
        return render(request, "password.html", {"result": "".join(result.generieren(16, True)), "form": form})

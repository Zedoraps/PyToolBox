from django.shortcuts import render

# Create your views here.
from calculator.calculator import GradeCalculator
from calculator.forms import CalculatorForm

grade_calc = GradeCalculator(max_points=100)


def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CalculatorForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            reached_points = form.cleaned_data['reached_points']
            max_points = form.cleaned_data['max_points']
            reset = form.cleaned_data['reset']
            global grade_calc
            if grade_calc.max_points != max_points or reset:
                grade_calc = GradeCalculator(max_points)

            result = grade_calc.calculate(reached_points)
            lowest = grade_calc.lowest()
            highest = grade_calc.highest()
            all_grades = grade_calc.all()
            avg = grade_calc.avg()
            return render(request, 'calculator.html',
                          {'form': form, "result": result, "lowest": lowest, "highest": highest,
                           "all_grades": all_grades, "avg": avg})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CalculatorForm()

        return render(request, 'calculator.html', {"form": form})

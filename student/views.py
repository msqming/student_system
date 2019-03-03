from django.shortcuts import render, HttpResponseRedirect
from student.models import Student
from student.forms import StudentForm


def index(request):
    students = Student.objects.all()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            student = Student()
            student.name = cleaned_data['name']
            student.sex = cleaned_data['sex']
            student.email = cleaned_data['email']
            student.profession = cleaned_data['prfession']
            student.qq = cleaned_data['qq']
            student.phone = cleaned_data['phone']
            student.save()
            return HttpResponseRedirect(reversed('index/'))
    else:
        form = StudentForm()

    context = {'students': students, 'form': form}
    # return render(request, 'index.html', context={'students': students})
    return render(request, 'index.html', context=context)

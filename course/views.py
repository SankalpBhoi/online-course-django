from django.shortcuts import render, redirect
from .models import Course, Question, Choice, Submission
from django.shortcuts import render


def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    return render(request, 'courses/course_details_bootstrap.html', {'course': course})


def submit(request):
    if request.method == "POST":
        score = 0
        questions = Question.objects.all()

        for question in questions:
            selected = request.POST.get(str(question.id))
            if selected:
                choice = Choice.objects.get(id=selected)
                if choice.is_correct:
                    score += 1

        return render(request, 'courses/result.html', {'score': score})

    questions = Question.objects.all()
    return render(request, 'courses/exam.html', {'questions': questions})


def show_exam_result(request):
    submissions = Submission.objects.all()
    return render(request, 'courses/show_result.html', {'submissions': submissions})


def final_result(request):
    return render(request, 'courses/result.html')
from django.shortcuts import render, redirect
from .models import Course, Question, Choice, Submission
from django.shortcuts import render


def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    return render(request, 'courses/course_details_bootstrap.html', {'course': course})


from django.shortcuts import render, redirect
from .models import Question, Choice, Submission, Enrollment, Course


def submit(request, course_id):
    if request.method == "POST":
        enrollment = Enrollment.objects.first()  # simple for assignment

        for question in Question.objects.all():
            selected_choice_id = request.POST.get(str(question.id))
            if selected_choice_id:
                choice = Choice.objects.get(id=selected_choice_id)
                Submission.objects.create(
                    enrollment=enrollment,
                    question=question,
                    selected_choice=choice
                )

        submission = Submission.objects.latest('id')

        return redirect('show_exam_result', course_id=course_id, submission_id=submission.id)

    questions = Question.objects.all()
    return render(request, 'courses/exam.html', {'questions': questions})


def show_exam_result(request, course_id, submission_id):
    submissions = Submission.objects.filter(id=submission_id)

    total_score = 0
    possible_score = submissions.count()

    for submission in submissions:
        if submission.is_get_score():
            total_score += 1

    context = {
        'total_score': total_score,
        'possible_score': possible_score
    }

    return render(request, 'courses/result.html', context)


def final_result(request):
    return render(request, 'courses/result.html')
from django.shortcuts import render, redirect
from .models import Image, UserAnswer


def quiz_view(request, question_number):
    if request.method == 'POST':
        user_answer = request.POST.get('user_answer')
        image_id = request.POST.get('image_id')
        image = Image.objects.get(pk=image_id)
        is_correct = user_answer == image.correct_answer
        UserAnswer.objects.create(user_answer=user_answer, is_correct=is_correct, image=image)

        if question_number < 20:
            return redirect('quiz_view', question_number=question_number + 1)
        else:
            correct_answers_count = UserAnswer.objects.filter(is_correct=True).count()
            return render(request, 'quiz/result.html')

    try:
        image = Image.objects.get(pk=question_number)
    except Image.DoesNotExist:

        return render(request, 'quiz/error.html', {'error_message': 'Image not found'})

    return render(request, 'quiz/quiz.html', {'image': image, 'question_number': question_number})

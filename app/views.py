from django.shortcuts import render, redirect


# Create your views here.

def index(request):
    data = {"inserted_text": "This text is inserted by server!"}
    return render(request, "index.html", context=data)


def take_question(request):
    if request.method == "GET":
        questionNum = request.GET.get('question-no')
        questionAnswer = request.GET.get('answer')
        print(questionAnswer)
        print(questionNum)
        request.session[questionNum] = questionAnswer
        nextQuestion = "http://127.0.0.1:8000/pitanje" + str(int(questionNum) + 1)
        print(nextQuestion)
        return redirect(nextQuestion, permanent=True)


def renderPitanje2(request):
    qa = request.session['1']
    return render(request, "pitanje2.html", context={'answer': qa})

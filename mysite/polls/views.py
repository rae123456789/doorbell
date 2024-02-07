from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from polls.models import Question, Choice
from django.template import loader
from django.http import Http404
from django.urls import reverse
# Create your views here.
# def home(request):
#     questions = Question.objects.all()
#     template = loader.get_template('polls/index.html')
#     html = ''
#     for question in questions:
#         html = html + f'<p> <a href="question/{question.id}">{question.question_text}</a> </p>'
#     context = {'questions': questions}
#     return HttpResponse(template.render )

def detail(request, question_id):
    question = Question.objects.get(id = question_id)
    choices = question.choice_set.all()
    template = loader.get_template('polls/detail.html')
    context = {'q': question, 'choices': choices}
    html = template.render(context, request)
    return HttpResponse(html)

    
def create_poll(request):
    print(request.POST)
    question = request.POST['question']
    choices = []
    for i in range(5):
        choices.append(request.POST['choice' + str(i+1)])

    print(choices)
    
    if question:
        question = Question.objects.create(question_text = question, author_name=request.user.username)

        for choice in choices:
            if choice:
                choice = Choice.objects.create(choice_text = choice, question = question)

    return redirect(request.META['HTTP_REFERER'])



    

def results(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'polls/results.html', {'q':question})

def vote(request, question_id):
    print(request.POST)
    choice_id = request.POST['choice']
    choice = Choice.objects.get(id=choice_id)
    choice.votes += 1
    choice.save()
    return HttpResponseRedirect(reverse('results', args=[question_id]))

    #return HttpResponse(f'You have voted for {choice.choice_text} - votes {choice.votes}')
    

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')

    context = {
        'question': latest_question_list,
    }
    return render(request,  'polls/index.html', context)
def practice(request):
    #q = Question(question_text = 'What school do you go to')
    #q.save()
    #return HttpResponse(q.id)
    qu = Question.objects.get(id = 21)
    return HttpResponse(qu.pub_date)
    





from django.http import HttpResponse
from .models import Choice, Question
#from django.template import loader
from django.shortcuts import render,get_object_or_404
from django.http import Http404

# Create your views here.
def index(request):
    all_question = Question.objects.all()
    #template = loader.get_template('polls/index.html')
    all_choice = Choice.objects.all()
    context={
        'all_question':all_question,
        'all_choice':all_choice
    }
    #return HttpResponse(template.render(context,request))


    return render(request, 'polls/index.html',context)

def detail(request,question_id):
    """try:
        question=Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question with id "+ str(question_id) +" does  not exixst")"""
    question =get_object_or_404(Question,pk=question_id)
    
    return render(request, 'polls/detail.html',{'question':question})


from django.shortcuts import render
from django.http import Http404
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator
from qa.models import Question
from qa.models import Answer


# Create your views here.

from django.http import HttpResponse
def test(request, *args, **kwargs):
	return HttpResponse('OK')

@require_GET
def mainpage(request, *args, **kwargs):
    question = Question.objects.all()
    #filter(rating__lt=1000)
    limit = 1
    page = request.GET.get('page', 1)
    paginator = Paginator(question,limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)

    #print(Question.objects.get(text='text1'))
    #print(paginator.)
    #t = get_template('mainpage.html')
    return render(request, 'mainpage.html', {
		'question': page.object_list,
		'paginator': paginator,
                'page': page,
	})


@require_GET
def popular(request, *args, **kwargs):
    question = Question.objects.all().order_by('-rating')
    limit = 1
    page = request.GET.get('page', 1)
    paginator = Paginator(question,limit)
    paginator.baseurl = '/popular/?page='
    page = paginator.page(page)
    return render(request, 'mainpage.html', {
        'question': page.object_list,
        'paginator': paginator,
        'page': page,
    })

@require_GET
def question(request, qid):
    idq = int(qid)
    question = Question.objects.get(id=idq)
    if question == None:
        return Http404
    else:
        answer = Answer.objects.all().filter(question=idq)
        if answer != None:
            return render(request, 'details.html',{
                'question': question,
                'answer': answer,
            })
        else:
            return render(request, 'details.html',{
                'question': question,
            })

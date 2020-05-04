from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse

from django.template import loader, RequestContext

from .models import Quiz, Category, Question, QuizViews

def index(request):
    exquizzes = Quiz.objects.order_by('hits')
    Quizzes = exquizzes.order_by('publicationDate')
    extrendingQuizzes = list(reversed(Quizzes))
    trendingQuizzes = extrendingQuizzes[:15]
    context = {
        'quizzes': trendingQuizzes,
        'pageNumber': 0,
        'group': "Trending",
        'range': range(len(trendingQuizzes)),
        'colored': 0
    }
    return render(request, 'quiz/index.html', context)

def quizzes(request):
    exQuizzes = Quiz.objects.order_by('title')[:12]
    Quizzes = list(reversed(exQuizzes))
    total = len(Quiz.objects.all())
    if total % 12 == 0:
        pages = int(total / 12)
    else:
        pages = int(total / 12 + 1)
    context = {
        'pages': range(pages + 1),
        'quizzes': Quizzes,
        'pageNumber': 1,
        'group': "All",
        'range': range(len(Quizzes)),
        'colored': 4
    }
    return render(request, 'quiz/index.html', context)


def allbypagenumber(request, pageNumber):
    exquizzes = Quiz.objects.order_by('title')[12*(pageNumber-1):12*pageNumber]
    Quizzes = list(reversed(exquizzes))
    total = len(Quiz.objects.all())
    if total % 12 == 0:
        pages = int(total / 12)
    else:
        pages = int(total / 12 + 1)
    context = {
        'pages': range(pages+1),
        'pageNumber': pageNumber,
        'quizzes': Quizzes,
        'group': "All",
        'range': range(len(Quizzes)),
        'colored': 0
    }
    return render(request, 'quiz/index.html', context)


def new(request):
    exnewestQuizzes = Quiz.objects.order_by('publicationDate')[:12]
    newestQuizzes = list(reversed(exnewestQuizzes))
    total = len(Quiz.objects.all())
    if total % 12 == 0:
        pages = int(total / 12)
    else:
        pages = int(total / 12 + 1)
    context = {
        'pages': range(pages+1),
        'pageNumber': 1,
        'quizzes': newestQuizzes,
        'group': "Newest",
        'range': range(len(newestQuizzes)),
        'colored': 1
    }
    return render(request, 'quiz/index.html', context)


def newbypagenumber(request, pageNumber):
    newestQuizzes = Quiz.objects.order_by('publicationDate')[12*(pageNumber-1):12*pageNumber]
    total = len(Quiz.objects.all())
    if total % 12 == 0:
        pages = int(total / 12)
    else:
        pages = int(total / 12 + 1)
    context = {
        'pages': range(pages+1),
        'pageNumber': pageNumber,
        'quizzes': newestQuizzes,
        'group': "Newest",
        'range': range(len(newestQuizzes)),
        'colored': 1
    }
    return render(request, 'quiz/index.html', context)


def popular(request):
    expopularQuizzes = Quiz.objects.order_by('hits')[:15]
    popularQuizzes = list(reversed(expopularQuizzes))
    total = len(Quiz.objects.all())
    if total % 12 == 0:
        pages = int(total / 12)
    else:
        pages = int(total / 12 + 1)
    context = {
        'pages': range(pages + 1),
        'pageNumber': 1,
        'quizzes': popularQuizzes,
        'group': "Popular",
        'range': range(len(popularQuizzes)),
        'colored': 2
    }
    return render(request, 'quiz/index.html', context)


def popularbypagenumber(request, pageNumber):
    popularQuizzes = Quiz.objects.order_by('hits')[12*(pageNumber-1):12*pageNumber]
    total = len(Quiz.objects.all())
    if total % 12 == 0:
        pages = int(total / 12)
    else:
        pages = int(total / 12 + 1)
    context = {
        'pages': range(pages+1),
        'pageNumber': pageNumber,
        'quizzes': popularQuizzes,
        'group': "Popular",
        'range': range(len(popularQuizzes)),
        'colored': 2
    }
    return render(request, 'quiz/index.html', context)

def categories(request):
    categories = Category.objects.order_by('text')
    context = {
        'categories': categories,
        'group': "Categories",
        'range': range(len(categories))
    }
    return render(request, 'quiz/categories.html', context)


def searchbyCategory(request, Category_id):
    results = Quiz.objects.filter(category__id=Category_id)[:12]
    Category_name = get_object_or_404(Category, id=Category_id).name
    context = {
        'quizzes': results,
        'group': Category_name,
        'colored': 3,
        'range': range(len(results))
    }
    return render(request, 'quiz/index.html', context)


def searchbycategorybypagenumber(request,Category_id, pageNumber):
    results = Quiz.objects.filter(category__id=Category_id).order_by('title')[12*(pageNumber-1):12*pageNumber]
    total = len(Quiz.objects.filter(category__id=Category_id))
    Category_name = get_object_or_404(Category, id=Category_id).name
    if total % 1 == 0:
        pages = int(total / 12)
    else:
        pages = int(total / 12 + 1)
    context = {
        'pages': range(pages+1),
        'pageNumber': pageNumber,
        'quizzes': results,
        'category_id': Category_id,
        'group': Category_name,
        'range': range(len(results)),
        'colored': 3
    }
    return render(request, 'quiz/index.html', context)


def search(request):
    query = request.GET.get('q')
    results = Quiz.objects.filter(Q(title__icontains=query) | Q(mainQuestion__icontains=query) | Q(description__icontains=query))
    context = {
        'quizzes': results,
        'group': "Results",
        'range': range(len(results)),
        'colored': 4
    }
    return render(request, 'quiz/index.html', context)


def startQuiz(request, Quiz_id):
    resultQuiz = Quiz.objects.get(id=Quiz_id)
    questions = Question.objects.filter(quiz=Quiz_id)
    quizViewed, created = QuizViews.objects.get_or_create(quiz=resultQuiz, ip=request.META['REMOTE_ADDR'])
    if created:
        quizViewed.quiz.hits += 1
        quizViewed.quiz.save()
    context = {
        'quiz': resultQuiz,
        'questions': questions,
        'length': len(questions)
    }
    return render(request, 'quiz/quiz.html', context)



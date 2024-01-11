from random import randint

from django.http import HttpResponse

from quiz.tasks import mine_bitcoin


def bitcoin(request):
    mine_bitcoin.delay(randint(1, 20))
    return HttpResponse("Task is started")

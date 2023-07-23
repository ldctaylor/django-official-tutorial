from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404


from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {
         "latest_question_list":latest_question_list,
         }
    return render(request, "polls/index.html", context)

# this was the original version before I rewrote it using render():
    # latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # template = loader.get_template("polls/index.html")
    # context = {
    #     "latest_question_list": latest_question_list,
    # }
    # return HttpResponse(template.render(context,request))

def detail(request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        return render(request,"polls/detail.html", {"question": question}) 

#detail view with long way of doing 404:
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question Does Not Exist")
#     return render(request,"polls/detail.html", {"question": question})

def results(request, question_id):
    response = "You're looking at the results of question %s." 
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the budget index.")

def add_expense(request):
    return HttpResponse("New Expense Page")

def edit_expense(request, expense_id):
    response = "You're looking at the results of expense %s."
    return HttpResponse(response % expense_id)
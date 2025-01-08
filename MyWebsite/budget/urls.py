from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("AddExpense", views.add_expense, name="add_expense"),
    path("EditExpense/<int:expense_id>", views.edit_expense, name="edit_expense"),
]
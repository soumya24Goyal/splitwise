from django.urls import path
from .views import EqualExpenseView

urlpatterns = [
    path('equal-expense_User/', EqualExpenseView.as_view(), name='equal-expense'),
]
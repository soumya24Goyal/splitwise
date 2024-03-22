from .models import User
from .models.expense import Expense
from .models.equal_expense import EqualExpense

class ExpenseService:
    @staticmethod
    def EqualExpenseService(expense_type, amount, paid_by, splits, metadata):
        if expense_type == 'EQUAL':
            total_splits = len(splits)
            split_amount = round(amount / total_splits, 2)
            for split in splits:
                split.amount = split_amount
            splits[0].amount += amount - split_amount * total_splits
            return EqualExpense.objects.create(amount=amount, paid_by=paid_by, metadata=metadata)
        else:
            return None

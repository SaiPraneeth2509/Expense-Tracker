from django.db import models

# Create your models here.
class Expense(models.Model):
    title = models.CharField(max_length=100)
    amount=models.DecimalField(max_digits=10, decimal_places=2)
    category=models.CharField(max_length=100)
    date=models.DateField()

    def __str__(self) -> str:
        return f"{self.title}-{self.amount}"

class Tag(models.Model):
    name = models.CharField(max_length=50)
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE, related_name='tags')

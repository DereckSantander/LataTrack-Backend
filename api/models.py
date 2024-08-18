from django.db import models
from django.contrib.auth.models import User

INCOME = 'ingreso'
EXPENSE = 'gasto'
CATEGORY_TYPES = [
    (INCOME, 'Ingreso'),
    (EXPENSE, 'Gasto'),
    ]

class Category(models.Model):

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=7, choices=CATEGORY_TYPES)
    #user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['type']
    def __str__(self):
        return self.name
    
class Report(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    startDate = models.DateTimeField()
    finishDate = models.DateTimeField()

    def assign_transactions(self):
        transactions_to_update = Transaction.objects.filter(
            created__gte=self.startDate,
            created__lte=self.finishDate,
            report__isnull=True
        )
        transactions_to_update.update(report=self)

    def save(self, *args, **kwargs):
        super(Report, self).save(*args, **kwargs)
        self.assign_transactions()

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title


class Transaction(models.Model):

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='transactions')
    created = models.DateTimeField()
    report = models.ForeignKey(Report, on_delete=models.CASCADE, related_name='transactions', null=True, blank=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f"{self.category.type} - {self.category.name} - {self.amount}"

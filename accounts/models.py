from django.db import models
from common.models import UserProfile
from django.contrib.auth.models import User
from invoice.models import Invoice

class AccountLedger(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='account_ledger'
    )
    invoice = models.ForeignKey(
        'Invoice', related_name='invoice_ledger', blank=True, null=True, on_delete=models.CASCADE
    )
    debit_amount = models.DecimalField(
        max_digits=65, decimal_places=2, default=0, blank=True, null=True
    )
    credit_amount = models.DecimalField(
        max_digits=65, decimal_places=2, default=0, blank=True, null=True
    )
    details = models.TextField(max_length=500, blank=True, null=True)
    status = models.BooleanField(default=True)
    dated = models.DateField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        return self.user
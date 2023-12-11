from django.db import models
from .enums import TicketPriority, TicketStatus
from django.utils import timezone
from model_utils.models import TimeStampedModel

# Create your models here.
class Ticket(models.Model, TimeStampedModel):
    title = models.CharField(max_length=100, blank=True,)
    description = models.TextField()
    priority = models.CharField(choices=TicketPriority.choices, blank=True)
    status = models.CharField(choices=TicketStatus.choices, default=TicketStatus.OPEN)
    due_date = models.DateTimeField(default=timezone.now)
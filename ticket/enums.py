from django.db import models

class TicketPriority(models.TextChoices):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"

class TicketStatus(models.TextChoices):
    OPEN = "Open"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
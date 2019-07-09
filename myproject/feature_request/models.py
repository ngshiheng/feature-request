from django.db.models import F
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Request(models.Model):
    CLIENT_A = 'Client A'
    CLIENT_B = 'Client B'
    CLIENT_C = 'Client C'
    CLIENT_CHOICES = [
        (CLIENT_A, 'A'),
        (CLIENT_B, 'B'),
        (CLIENT_C, 'C'),
    ]

    ASSESSMENTS = 'Assessments'
    BILLING = 'Billing'
    RECRUIT = 'Recruit'
    REPORTS = 'Reports'
    PRODUCT_AREA_CHOICES = [
        (ASSESSMENTS, 'Assessments'),
        (BILLING, 'Billing'),
        (RECRUIT, 'Recruit'),
        (REPORTS, 'Reports'),
    ]

    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    client = models.CharField(
        max_length=10,
        choices=CLIENT_CHOICES,
        default=CLIENT_A,
    )
    priority = models.PositiveIntegerField()
    target_date = models.DateField(default=timezone.now(), editable=True, null=False, blank=False)
    product_area = models.CharField(
        max_length=20,
        choices=PRODUCT_AREA_CHOICES,
        default=ASSESSMENTS,
    )

    def reorder_priority(self):
        existing_feature = Request.objects.get(priority=self.priority)
        foo = Request.objects.filter(priority__gte=existing_feature.priority)
        foo.update(priority=F('priority') + 1)
        foo.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('request-create')

    class Meta:
        verbose_name_plural = "requests"

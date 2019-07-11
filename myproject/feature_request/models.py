from django.db.models import F
from django.db import models


class ProductArea(models.Model):
    product_area = models.CharField(max_length=20)

    def __str__(self):
        return self.product_area

    class Meta:
        verbose_name = "Product Area"


class Client(models.Model):
    client = models.CharField(max_length=50)

    def __str__(self):
        return self.client

    class Meta:
        ordering = ['client']


class Request(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    priority = models.PositiveIntegerField()
    target_date = models.DateField(editable=True, null=False, blank=False)
    product_area = models.ForeignKey(ProductArea, on_delete=models.CASCADE)

    def save(self, **kwargs):

        # check if the priority has already existed:
        try:
            existing_feature_priority = Request.objects.get(priority=self.priority).priority
            current_priorities = Request.objects.filter(priority__gte=existing_feature_priority)
            if current_priorities.count() > 0:
                current_priorities.update(priority=F('priority') + 1)

            super(Request, self).save(**kwargs)

        # if the priority does not exist:
        except:
            least_priority_feature = Request.objects.all().last().priority

            if int(self.priority) > least_priority_feature:
                self.priority = least_priority_feature + 1
            super(Request, self).save(**kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['priority']

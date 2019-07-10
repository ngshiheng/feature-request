from django.db.models import F
from django.db import models
from django.urls import reverse


class ProductArea(models.Model):
    product_area = models.CharField(max_length=20)

    def __str__(self):
        return self.product_area


class Client(models.Model):
    client = models.CharField(max_length=50)

    def __str__(self):
        return self.client


class Request(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    priority = models.PositiveIntegerField()
    target_date = models.DateField(editable=True, null=False, blank=False)
    product_area = models.ForeignKey(ProductArea, on_delete=models.CASCADE)

    def save(self, **kwargs):
        # try to check if there is any existing priority that is duplicated:
        try:
            existing_feature = Request.objects.get(priority=self.priority)
            foo = Request.objects.filter(priority__gte=existing_feature.priority)
            if foo.count() > 0:
                foo.update(priority=F('priority') + 1)

            super(Request, self).save(**kwargs)

        except:
            super(Request, self).save(**kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        url = reverse('request-create')
        return url

    class Meta:
        verbose_name_plural = "requests"
        ordering = ["priority"]

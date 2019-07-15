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

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['priority']

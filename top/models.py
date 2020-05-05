from django.db import models


class ApiVieu(models.Model):
    id = models.SlugField(blank=False, primary_key=True)
    type = models.CharField(max_length=300)
    url = models.URLField(max_length=300)
    created_at = models.DateField( auto_now_add=True)
    company = models.CharField(max_length=500)
    company_url = models.URLField(max_length=100, null=True)
    location = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    description = models.TextField()

    def __str__(self):
        return self.title

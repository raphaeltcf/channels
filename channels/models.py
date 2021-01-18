from django.db import models


class Channel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    link = models.URLField()

    def __str__(self):
        return self.title


class Item(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    link = models.URLField()
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title
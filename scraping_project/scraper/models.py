from django.db import models

class Job(models.Model):
    job_id = models.UUIDField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Task(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    coin = models.CharField(max_length=255)
    output = models.JSONField()
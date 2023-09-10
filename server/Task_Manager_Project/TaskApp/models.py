from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    client = models.CharField(max_length=100)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
        
    

class Tasks(models.Model):
    STATUS = (
        ('TODO', 'To DO'),
        ('WIP', 'Work in Progress'),
        ('ONHOLD', 'On Hold'),
        ('DONE', 'Complete'),
    )

    name = models.CharField(max_length=150)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks_set')
    status = models.CharField(max_length=10, choices=STATUS)

    def __str__(self):
        return self.name


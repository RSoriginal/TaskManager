from django.db import models

class Category(models.Model):
    categoryName = models.CharField(max_length=255)

    def __str__(self):
        return self.categoryName

class Task(models.Model):
    STATUS_CHOICES = [
        ('in_progress', 'В роботі'),
        ('completed', 'Завершено'),
        ('pending', 'Очікує'),
    ]
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()
    priority = models.IntegerField()
    status = models.CharField(
        max_length=12,
        choices=STATUS_CHOICES,
        default='pending',
    )
    creationDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
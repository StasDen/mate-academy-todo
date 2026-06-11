from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Task(models.Model):
    content = models.CharField(blank=True, max_length=15)  # NOTE: I would rather increase max_length. The current value is more suitable for tags
    created_at = models.DateTimeField(auto_now_add=True)
    # FIXME
    # According to the task description, this field must be optional.
    # Hint: use 'null' and 'blank' parameters, then perform migration to override existing 'NOT NULL' database constraint
    deadline = models.DateTimeField()  

    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(to=Tag, related_name="tasks")

    class Meta:
        # FIXME
        # Change the order to the required one: from NOT DONE to DONE and from NEWEST to OLDEST.
        # Hint: to apply reverse order, use a '-' prefix
        ordering = ["created_at", "is_done"]

    def __str__(self):
        return f"Content: {self.content}"

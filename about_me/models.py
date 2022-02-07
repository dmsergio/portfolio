from django.db import models
from django.contrib.auth.models import User


class CurriculumVitae(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="curriculum",
    )
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"CV: {self.user.first_name}"

    def __repr__(self):
        return (f"<{self.__class__.__name__}: "
                f"{self.user.first_name} ({self.id})>")


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.name} ({self.id})>"


class Job(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    tasks = models.ManyToManyField(Task, related_name="jobs")
    curriculum = models.ForeignKey(
        CurriculumVitae,
        on_delete=models.CASCADE,
        related_name="jobs",
    )

    def __str__(self):
        return f"{self.name} at {self.company[:20]}"

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.name} ({self.id})>"


class Study(models.Model):
    class Meta:
        ordering = ["-start_date"]

    name = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)
    curriculum = models.ForeignKey(
        CurriculumVitae,
        on_delete=models.CASCADE,
        related_name="studies",
    )

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.name} ({self.id})>"


class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    curriculum = models.ForeignKey(
        CurriculumVitae,
        on_delete=models.CASCADE,
        related_name="skills",
    )

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.name} ({self.id})>"


class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    curriculum = models.ForeignKey(
        CurriculumVitae,
        on_delete=models.CASCADE,
        related_name="programming_languages",
    )

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.name} ({self.id})>"


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    curriculum = models.ForeignKey(
        CurriculumVitae,
        on_delete=models.CASCADE,
        related_name="library",
    )

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.name} ({self.id})>"

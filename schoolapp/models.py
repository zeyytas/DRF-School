
from django.db import models


class Exam(models.Model):
    date = models.DateField()
    student_name = models.CharField(max_length=100)
    score = models.IntegerField()
    course_name = models.CharField(max_length=100)
    teacher_name = models.CharField(max_length=100)

    def __str__(self):
        return '{} {} {}'.format(self.date, self.student_name, self.score)
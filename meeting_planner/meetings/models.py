from django.db import models
from django.utils import timezone
from datetime import time, datetime
from django.core.exceptions import ValidationError


def validate_geq1(value):
    if value < 1:
        raise ValidationError(message=f"{value} is not at least 1")


class Room(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200)
    floor_number = models.PositiveSmallIntegerField(validators=[validate_geq1])
    room_number = models.PositiveIntegerField(validators=[validate_geq1])

    def __str__(self):
        return f"{self.name.title()}: room {self.room_number} on floor {self.floor_number}"


class Meeting(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    date = models.DateField(default=None, blank=True, null=True)
    start_time = models.TimeField(default=timezone.now)
    duration_minutes = models.IntegerField(default=0)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title.title()} for {self.duration_minutes} minutes at {self.start_time} on {self.date}"

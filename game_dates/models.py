from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Any Amends to choices needs to be added to templates/booking
SERVICE_CHOICES = (
    ("Online gaming", "Online Gaming"),
    ("In person gaming", "In person gaming"),
    ("Watch party", "Watch party"),
    ("Board games", "Board games"),
    )
TIME_CHOICES = (
    ("12 AM", "12 AM"),
    ("1 AM", "1 AM"),
    ("2 AM", "2 AM"),
    ("3 AM", "3 AM"),
    ("4 AM", "4 AM"),
    ("5 AM", "5 AM"),
    ("6 AM", "6 AM"),
    ("7 AM", "7 AM"),
    ("8 AM", "8 AM"),
    ("9 AM", "9 AM"),
    ("10 AM", "10 AM"),
    ("11 AM", "11 AM"),
    ("12 PM", "12 PM"),
    ("1 PM", "1 PM"),
    ("2 PM", "2 PM"),
    ("3 PM", "3 PM"),
    ("4 PM", "4 PM"),
    ("5 PM", "5 PM"),
    ("6 PM", "6 PM"),
    ("7 PM", "7 PM"),
    ("8 PM", "8 PM"),
    ("9 PM", "9 PM"),
    ("10 PM", "10 PM"),
    ("11 PM", "11 PM"),
)


class Appointment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    type = models.CharField(
        max_length=50, choices=SERVICE_CHOICES, default="Online gaming")
    day = models.DateField(default=datetime.now)
    time = models.CharField(
        max_length=24, choices=TIME_CHOICES)
    updated_on = models.DateTimeField(auto_now=True)
    description = models.CharField(
        max_length=50, null=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)
    attending = models.ManyToManyField(
        User, related_name='event_attending', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.user.username} | day: {self.day} | time: {self.time}"

    def number_of_attendees(self):
        return self.attending.count()

    def number_of_tentative(self):
        return self.tentative.count()


class Comment(models.Model):
    post = models.ForeignKey(Appointment, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField(blank=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

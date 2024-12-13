from django.db import models

# Create your models here.

# User Model
class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=255)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

# Event Model
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_time = models.DateTimeField()
    location = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="events_created")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# Registration Model
class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)
    ticket_type = models.CharField(max_length=50)
    number_of_tickets = models.PositiveIntegerField()

    def __str__(self):
        return f"Registration of {self.user.username} for {self.event.title}"

# Notification Model
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username}"

# Payment Model
class Payment(models.Model):
    registration = models.OneToOneField(Registration, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for {self.registration.id}"

# Venue Model
class Venue(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    capacity = models.PositiveIntegerField()
    contact_info = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Ticket Model
class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    availability = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.type} Ticket for {self.event.title}"

# Review Model
class Review(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.event.title}"

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

# EventCategory Model
class EventCategory(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.event.title} - {self.category.name}"


from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from django.shortcuts import render
from .models import Registration
from rest_framework.response import Response
from .models import Event
from .serializers import EventSerializer
from rest_framework import viewsets

from .models import User, Event, Registration, Notification, Payment, Venue, Ticket, Review, Category, EventCategory
from .serializers import (
    UserSerializer, EventSerializer, RegistrationSerializer, NotificationSerializer, PaymentSerializer, 
    VenueSerializer, TicketSerializer, ReviewSerializer, CategorySerializer, EventCategorySerializer
)
from rest_framework.permissions import IsAuthenticated
import requests

# Create your views here.

def send_event_notification(event_id, message):
    url = "https://final-project-444515.cloudfunctions.net/notify_users"
    payload = {"event_id": event_id, "message": message}
    response = requests.post(url, json=payload)
    return response.json()

def register_for_event(request):
    # Process registration
    event_id = request.POST.get("event_id")
    message = "Thank you for registering for the event!"

    # Call Cloud Function
    response = send_event_notification(event_id, message)

    return JsonResponse(response)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class VenueViewSet(viewsets.ModelViewSet):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class EventCategoryViewSet(viewsets.ModelViewSet):
    queryset = EventCategory.objects.all()
    serializer_class = EventCategorySerializer

class EventList(APIView):
    """
    List all events
    """
    def get(self, request, format=None):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

class EventDetail(APIView):
    """
    Retrieve, update or delete a specific event
    """
    def get(self, request, pk, format=None):
        try:
            event = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = EventSerializer(event)
        return Response(serializer.data)

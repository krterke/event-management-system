"""
URL configuration for event_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from events.views import (
    UserViewSet, EventViewSet, RegistrationViewSet, NotificationViewSet, 
    PaymentViewSet, VenueViewSet, TicketViewSet, ReviewViewSet, 
    CategoryViewSet, EventCategoryViewSet
)
from .views import EventList, EventDetail

# Create a router and register viewsets
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'events', EventViewSet)
router.register(r'registrations', RegistrationViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'venues', VenueViewSet)
router.register(r'tickets', TicketViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'event-categories', EventCategoryViewSet)

# Define URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # All API endpoints will be prefixed with /api/
     path('api/events/', EventList.as_view(), name='event-list'),
    path('api/events/<int:pk>/', EventDetail.as_view(), name='event-detail'),
]


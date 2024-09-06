from django.urls import path, include

from notification.api.views import send_message

urlpatterns = [
    path("send-message/", send_message, name="send_message"),
]

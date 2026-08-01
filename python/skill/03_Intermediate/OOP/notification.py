#notification system
from abc import ABC, abstractmethod

class Notification(ABC):

    @abstractmethod
    def send(self, message):
        pass
1
class EmailNotification(Notification):
     def send(self, message):
         print(f"Email sent: {message}")

class SMSNotification(Notification):
    def send(self, message):
         print(f"Sms sent: {message}")

class PushNotification(Notification):
     def send(self, message):
         print(f"Push sent: {message}")

message = "Hello user"
    
email = EmailNotification()
email.send(message)

sms = SMSNotification()
sms.send(message)

push = PushNotification()
push.send(message)


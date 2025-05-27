from typing import List, Dict
from .models import Notification
from datetime import datetime

class NotificationDatabase:
    def __init__(self):
        self.notifications: Dict[str, List[Notification]] = {}

    # Добавить уведомление
    def add_notification(self, email: str, message: str) -> Notification:
        notification = Notification(email=email, message=message)

        if email not in self.notifications:
            self.notifications[email] = []

        self.notifications[email].append(notification)
        return notification

    # Получить список уведомлений пользователя по его электронной почте
    def get_notifications(self, email: str) -> List[Notification]:
        return self.notifications.get(email, [])

from .database import NotificationDatabase

class NotificationService:
    def __init__(self):
        self.db = NotificationDatabase()

    # Отправить уведомление
    def send_notification(self, email: str, message: str) -> bool:
        notification = self.db.add_notification(email, message)
        return notification is not None

    # Получить список уведомлений
    def get_notifications(self, email: str) -> list:
        return self.db.get_notifications(email)

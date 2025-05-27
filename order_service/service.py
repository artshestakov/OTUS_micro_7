from .database import OrderDatabase
from billing_service.service import BillingService
from notification_service.service import NotificationService
from .models import OrderStatus

class OrderService:
    def __init__(self):
        self.db = OrderDatabase()
        self.billing = BillingService()
        self.notification = NotificationService()

    def create_user(self, user_id: str, email: str) -> bool:
        # Создаем аккаунт в биллинге при создании пользователя
        return self.billing.create_account(user_id)

    def create_order(self, order_id: str, user_id: str, price: float, email: str) -> bool:
        # Создаем заказ
        order = self.db.create_order(order_id, user_id, price)

        if not order:
            return False

        # Пытаемся списать деньги
        payment_success = self.billing.withdraw(user_id, price)

        if payment_success:
            # Обновляем статус заказа
            self.db.update_order_status(order_id, OrderStatus.PAID.value)

            # Отправляем письмо счастья
            self.notification.send_notification(email, f"Ваш заказ {order_id} успешно оплачен! Сумма: {price}")
        else:
            # Обновляем статус заказа
            self.db.update_order_status(order_id, OrderStatus.FAILED.value)

            # Отправляем письмо горя
            self.notification.send_notification(email, f"Не удалось оплатить заказ {order_id}. Недостаточно средств.")

        return True

    def get_order_status(self, order_id: str) -> str:
        order = self.db.get_order(order_id)
        return order.status if order else None

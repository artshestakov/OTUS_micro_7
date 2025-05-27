from typing import Dict
from .models import Order

class OrderDatabase:
    def __init__(self):
        self.orders: Dict[str, Order] = {}

    # Создание заказа
    def create_order(self, order_id: str, user_id: str, price: float) -> Order:
        order = Order(order_id=order_id, user_id=user_id, price=price)
        self.orders[order_id] = order
        return order

    # Получить заказ по его идентификатору
    def get_order(self, order_id: str) -> Order:
        return self.orders.get(order_id)

    # Обновить статус заказа
    def update_order_status(self, order_id: str, status: str) -> bool:
        order = self.get_order(order_id)

        if not order:
            return False

        order.status = status
        return True

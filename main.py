from order_service.service import OrderService

def main():
    # Инициализируем сервис заказов
    order_service = OrderService()

    # Создаем пользователя (автоматически создается аккаунт в биллинге)
    user_id = "user123"
    email = "user@example.com"
    order_service.create_user(user_id, email)

    # Пополняем баланс пользователя
    order_service.billing.deposit(user_id, 1000.0)
    print(f"Баланс пользователя: {order_service.billing.get_balance(user_id)}")

    # Создаем и оплачиваем заказ (успешно)
    order_id1 = "order456"
    order_service.create_order(order_id1, user_id, 500.0, email)
    print(f"Статус заказа {order_id1}: {order_service.get_order_status(order_id1)}")
    print(f"Баланс после заказа: {order_service.billing.get_balance(user_id)}")

    # Просматриваем уведомления
    notifications = order_service.notification.get_notifications(email)
    print("Уведомления:")
    for notification in notifications:
        print(f"- {notification.message}")

    # Пытаемся создать заказ с недостаточным балансом
    order_id2 = "order789"
    order_service.create_order(order_id2, user_id, 1000.0, email)
    print(f"Статус заказа {order_id2}: {order_service.get_order_status(order_id2)}")
    print(f"Баланс после второго заказа: {order_service.billing.get_balance(user_id)}")

    # Просматриваем уведомления
    notifications = order_service.notification.get_notifications(email)
    print("\nВсе уведомления:")
    for notification in notifications:
        print(f"- {notification.message}")

if __name__ == "__main__":
    main()

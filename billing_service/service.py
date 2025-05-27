from .database import BillingDatabase

class BillingService:
    def __init__(self):
        self.db = BillingDatabase()

    # Создание аккаунта
    def create_account(self, user_id: str) -> bool:
        account = self.db.create_account(user_id)
        return account is not None

    # Положить деньги на баланс пользователя
    def deposit(self, user_id: str, amount: float) -> bool:
        return self.db.update_balance(user_id, amount)

    # Снять деньги с баланса пользователя
    def withdraw(self, user_id: str, amount: float) -> bool:
        return self.db.update_balance(user_id, -amount)

    # Получить баланс пользователя
    def get_balance(self, user_id: str) -> float:
        account = self.db.get_account(user_id)
        return account.balance if account else 0.0

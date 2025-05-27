from typing import Dict
from .models import Account

class BillingDatabase:
    def __init__(self):
        self.accounts: Dict[str, Account] = {}

    # Создание аккаунта
    def create_account(self, user_id: str) -> Account:
        if user_id not in self.accounts:
            self.accounts[user_id] = Account(user_id=user_id)

        return self.accounts[user_id]

    # Получить аккаунт по идентификатору пользоваля
    def get_account(self, user_id: str) -> Account:
        return self.accounts.get(user_id)

    # Изменить баланс пользователя по его идентификатору
    def update_balance(self, user_id: str, amount: float) -> bool:
        account = self.get_account(user_id)

        if not account:
            return False

        if account.balance + amount < 0:
            return False

        account.balance += amount
        return True

from dataclasses import dataclass
from enum import Enum
from datetime import datetime

class OrderStatus(Enum):
    CREATED = "created"
    PAID = "paid"
    FAILED = "failed"

@dataclass
class Order:
    order_id: str
    user_id: str
    price: float
    status: OrderStatus = OrderStatus.CREATED
    created_at: datetime = datetime.now()

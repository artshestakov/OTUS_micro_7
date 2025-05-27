from dataclasses import dataclass
from datetime import datetime

@dataclass
class Notification:
    email: str
    message: str
    timestamp: datetime = datetime.now()
    is_sent: bool = True  # Фиктивно

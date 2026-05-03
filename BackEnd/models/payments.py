from database.db import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Enum, ForeignKey, DateTime, CheckConstraint
from datetime import datetime

class Payment(Base):
    __tablename__ = "payments"
    payment_id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.order_id"), nullable=False, index=True)
    amount: Mapped[int] = mapped_column(nullable=False)
    status: Mapped[str] = mapped_column(Enum("Da thanh toan", "Chua thanh toan", "Thanh toan that bai"), nullable=False, default="Chua thanh toan")
    method: Mapped[str] = mapped_column(String(255), nullable=False)
    transaction_id : Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.utcnow, index=True)

    __table_args__ = (
        CheckConstraint('amount > 0', name='check_amount_positive'),
    )



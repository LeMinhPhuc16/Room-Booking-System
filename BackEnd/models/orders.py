from database.db import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Enum, ForeignKey, DateTime, CheckConstraint 
from datetime import datetime

class Order(Base):
    __tablename__ = "orders"
    order_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"), nullable=False)
    total_price: Mapped[int] = mapped_column(nullable=False)  #  Tổng giá trị tại thời điểm đặt
    status: Mapped[str] = mapped_column(Enum("Da thanh cong", "Chua thanh cong", "Da huy"), nullable=False, default="Chua thanh cong")
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now)

    __table_args__ = (
        CheckConstraint('total_price > 0', name='check_total_price_positive'),
    )


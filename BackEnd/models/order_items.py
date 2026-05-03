from database.db import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, CheckConstraint

class OrderItem(Base):
    __tablename__ = "order_items"
    item_id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.order_id"), nullable=False)
    booking_id: Mapped[int] = mapped_column(ForeignKey("bookings.booking_id"), nullable=False)
    price: Mapped[int] = mapped_column(nullable=False)

    __table_args__ = (
        CheckConstraint("price > 0", name="check_price_ order_item_positive"),
    )
    




from sqlalchemy import String, ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column
from database.db import Base


class Room(Base):
    __tablename__ = "rooms"
    room_id: Mapped[int] = mapped_column(primary_key=True)
    room_name: Mapped[str] = mapped_column(String(50), nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.category_id"), nullable=False, index=True)
    capacity: Mapped[int] = mapped_column(nullable=False)
    price: Mapped[int] = mapped_column(nullable=False)    

    __table_args__ = (
        CheckConstraint("capacity > 0", name="check_capacity_positive"),
        CheckConstraint("price > 0", name="check_price_room_positive"),
    )